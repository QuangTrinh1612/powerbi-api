from powerbi.auth import PowerBiAuth
from powerbi.session import PowerBiSession
from powerbi.client import PowerBiClient
from powerbi.logger import get_logger
from powerbi.config import TENANT_ID, CLIENT_ID, CLIENT_SECRET

logger = get_logger("main")

def main():
    logger.info("Starting Power BI API client application.")
    try:
        auth = PowerBiAuth(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
        session = PowerBiSession(auth)
        client = PowerBiClient(session)
        
        group = client.groups()
        workspaces = group.get_groups()
        logger.info("Workspaces retrieved successfully: %s", workspaces)
    except Exception as e:
        logger.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()