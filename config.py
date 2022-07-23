import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_NAME= "127.0.0.1:7001"
    DEBUG = True
    
    DATABASE_PATH = "src/database/personas"
    DB_TOKEN = os.environ.get("DB_TOKEN","")
    ENCRYPT_DB = True
    
    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"