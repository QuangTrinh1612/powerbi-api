from powerbi.auth import PowerBiAuth
from powerbi.logger import get_logger

from typing import Dict
import requests
import json

class PowerBiSession():
    
    """Serves as the Session for the Current Microsoft
    Power Bi API."""
    
    def __init__(self, auth: PowerBiAuth) -> None:
        self.auth = auth
        self.resource_url = 'https://api.powerbi.com/'
        self.version = 'v1.0/'
        self.logger = get_logger(self.__class__.__name__)

    def get_headers(self) -> Dict:
        headers = {
            "Authorization": "Bearer {access_token}".format(access_token=self.auth.get_token()),
            "Content-Type": "application/json"
        }
        return headers
    
    def get_url(self, endpoint: str) -> str:
        url = self.resource_url + self.version + endpoint
        return url
    
    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict = {},
        data: dict = {},
        json_payload: dict = {}
    ):
        # Build the URL.
        url = self.get_url(endpoint=endpoint)

        # Define the headers.
        headers = self.get_headers()

        self.logger.info("URL: {url}".format(url=url))

        # Define a new session.
        request_session = requests.Session()
        request_session.verify = True

        # Define a new request.
        request = requests.Request(
            method=method.upper(),
            headers=headers,
            url=url,
            params=params,
            data=data,
            json=json_payload
        ).prepare()

        # Send the request.
        response: requests.Response = request_session.send(
            request=request
        )

        # Close the session.
        request_session.close()

        # If it's okay and no details.
        if response.ok and len(response.content) > 0 and response.headers['Content-Type'] != 'application/zip':
            return response.json()
        
        elif response.ok and len(response.content) > 0 and response.headers['Content-Type'] == 'application/zip':
            return response.content

        elif len(response.content) > 0 and response.ok:
            return {
                'message': 'response successful',
                'status_code': response.status_code
            }

        elif not response.ok:
            if len(response.content) == 0:
                response_data = ''
            else:
                response_data = response.json()

            response.request.headers['Authorization'] = 'Bearer XXXXXXX'

            # Define the error dict.
            error_dict = {
                'error_code': response.status_code,
                'response_url': response.url,
                'response_body': response_data,
                'response_request': dict(response.request.headers),
                'response_method': response.request.method,
            }

            # Log the error.
            self.logger.error(msg=json.dumps(obj=error_dict, indent=4))

            raise requests.HTTPError()