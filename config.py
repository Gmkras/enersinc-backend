import os
from dotenv import load_dotenv

load_dotenv()

class config:
    SERVER_NAME= "localhost:7001"
    DEBUG = True
    
    DATABASE_PATH = "app/database/personas"
    DB_TOKEN = os.environ.get("DB_TOKEN","")
    ENCRYPT_DB = True
    
    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"