import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv(".env"))

API_BASE_URL = "https://api.powerbi.com/v1.0/myorg"
TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")