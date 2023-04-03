from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# for the raw sql connection that we pasted below
# import time
# import psycopg2
# from psycopg2.extras import RealDictCursor
from app.config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# then we need to create an engine to create the onnection to the DB

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# when we actaully want to talk to the DB we need to make use of a session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



