import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

APP_PORT = os.environ.get("APP_PORT")
IP_SERVER = os.environ.get("IP_SERVER")

CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS")
ENDPOINT_URI = os.environ.get("ENDPOINT_URI")
CHAIN_ID = int(os.environ.get("CHAIN_ID"))
ABI_PATH = os.environ.get("ABI_PATH")

USER_WALLET = os.environ.get("USER_WALLET")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
