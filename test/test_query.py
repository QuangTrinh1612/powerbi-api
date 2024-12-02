from azure.identity import ClientSecretCredential
import json, requests

from powerbi.config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, WORKSPACE_ID, DATASET_ID

api = 'https://analysis.windows.net/powerbi/api/.default'
# --------------------------------------------------------------------------------------#

# Generates the access token for the Service Principal
auth = ClientSecretCredential(
    authority = 'https://login.microsoftonline.com/',
    tenant_id = TENANT_ID,
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET
)

access_token = auth.get_token(api)
access_token = access_token.token

print('\nSuccessfully authenticated.')   

#########################################################################################
# Query DAX result
#########################################################################################

base_url = 'https://api.powerbi.com/v1.0/myorg/'
headers = {'Authorization': f'Bearer {access_token}', 'Content-type': 'application/json'}
json_payload = {
    "queries": [
        {
            "query": "EVALUATE 'Dim Region'"
        }
    ]
}

result1 = requests.get(url=f"{base_url}groups/{WORKSPACE_ID}/datasets", headers=headers)
print(json.loads(result1.content))

# HTTP GET Request
result = requests.post(url=f"{base_url}groups/{WORKSPACE_ID}/datasets/{DATASET_ID}/executeQueries", headers=headers, json=json_payload)

# Response code (200 = Success; 401 = Unauthorized; 404 = Bad Request)
print(json.loads(result.content))

# Try to print the result
try:
    data = json.loads(result.content)

    # Pretty-prints the JSON
    print(json.dumps(data, indent=4, sort_keys=True))
        
except Exception as e:
    print('\nRequest failed:', e)