from fastapi import FastAPI, APIRouter
from database.base import Base
from database.db import engine
from backend.chore.config import settings

app = FastAPI()

app.add_api_route('users',APIRouter(),tags=['users'])
app.add_api_route('posts',APIRouter(),tags=['posts'])
app.add_api_route('chats',APIRouter(),tags=['chats'])

def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}