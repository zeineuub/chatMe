from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# connection url
SQLALCHEMY_DATABSE_URL= settings.DB_URL

# create an engine responsable to connect sqlachamy to postgres
engine = create_engine(SQLALCHEMY_DATABSE_URL)
# for evry db request a create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# for each db request a create a base
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()