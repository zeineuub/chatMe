from fastapi import FastAPI, APIRouter
from database.base import Base
from database.db import engine
from backend.utils.config import settings
from routes.users import router as users_router
from routes.authentication import router as auth_router

def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    app.include_router(users_router, prefix="/api/v1/users")
    app.include_router(auth_router, prefix="/api/v1/auth")
    return app

app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}