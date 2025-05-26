import os
from dotenv import load_dotenv

# loading api key from environment file
load_dotenv()


CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")

# the scope is a list so I opt to use split
SCOPES = os.getenv("SCOPES", "").split()

