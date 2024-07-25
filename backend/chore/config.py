
# to not directly communicate with the .env file
import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
class Settings:
    POSTGRES_USER:str=os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:str=os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str=os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT:int=os.getenv('POSTGRES_PORT')
    POSTGRES_DB:str=os.getenv('POSTGRES_DB')
    DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    PROJECT_NAME:str=os.getenv('PROJECT_NAME')
    PROJECT_VERSION:str=os.getenv('PROJECT_VERSION')
settings =Settings()