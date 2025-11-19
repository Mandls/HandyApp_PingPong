# from sqlalchemy import select
# from sqlalchemy.orm import Session

# from .config import settings
# from app.database.session import engine

# # models must be imported and registered from app.models to create the tables
# from app.database.session import Base, engine

# from app.schemas import snack as snack_schema

# # from app.crud import snack as snack_crud

# from app.models.snack import Snack

# def init_db(session: Session) -> None:
#   # Create tables
#   Base.metadata.create_all(bind=engine) 
