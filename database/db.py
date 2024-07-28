from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.utils.config import settings

# connection url
SQLALCHEMY_DATABSE_URL = settings.DB_URL

# create an engine responsable to connect sqlachamy to postgres
engine = create_engine(SQLALCHEMY_DATABSE_URL)
# for evry db request a create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
