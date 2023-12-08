import os
from dotenv import load_dotenv

load_dotenv()

DB_LOGIN = os.getenv('DB_LOGIN')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DJ_SECRET = os.getenv("DJ_SECRET")

UVCRN_HOST = os.getenv('UVCRN_HOST')
UVCRN_PORT = os.getenv('UVCRN_PORT')
SSL_KEYFILE = os.getenv('SSL_KEYFILE')
SSL_SERTIF = os.getenv('SSL_SERTIF')