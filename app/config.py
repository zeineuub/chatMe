
# to not directly communicate with the .env file
import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
class Settings:
    POSTGRES_USER:str=os.get('POSTGRES_USER')
    POSTGRES_PASSWORD:str=os.get('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str=os.get('POSTGRES_SERVER')
    POSTGRES_PORT:int=os.get('POSTGRES_PORT')
    POSTGRES_DB:str=os.get('POSTGRES_DB')
    DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
settings =Settings()