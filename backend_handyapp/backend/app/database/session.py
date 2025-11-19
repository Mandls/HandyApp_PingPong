from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="changethis",
    host="localhost",
    database="handyapp",
    port=5432
)

engine = create_engine(url)
Base = declarative_base()