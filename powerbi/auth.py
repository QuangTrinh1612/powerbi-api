from azure.identity import ClientSecretCredential
from powerbi.logger import get_logger

class PowerBiAuth:
    api_endpoint = 'https://analysis.windows.net/powerbi/api/.default'
    
    def __init__(
        self,
        tenant_id:str,
        client_id: str,
        client_secret: str
    ):
        """Initializes the `PowerBiAuth` Client.

        ### Parameters
        ----
        tenant_id: str
            The Tenant ID

        client_id : str
            The application Client ID assigned when
            creating a new Microsoft App.

        client_secret : str
            The application Client Secret assigned when
            creating a new Microsoft App.
        """

        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.logger = get_logger(self.__class__.__name__)

    def authenticate(self):
        self.logger.info("Starting authentication process.")
        
        try:
            auth = ClientSecretCredential(
                tenant_id = self.tenant_id,
                client_id = self.client_id,
                client_secret = self.client_secret
            )
            token = auth.get_token(self.api_endpoint).token
            self.access_token = token
            self.logger.info("Authentication successful.")

        except Exception as e:
            self.logger.error("Authentication failed: %s", e)
            raise e
        
    def get_token(self) -> str:
        if not self.access_token:
            self.logger.debug("No token found, initiating authentication.")
            self.authenticate()
        else:
            self.logger.debug("Using cached token.")
        return self.access_token