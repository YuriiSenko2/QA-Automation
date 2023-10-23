from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("postgresql+psycopg2://postgres:Mypassword12345@localhost:5432/postgres")

__session = sessionmaker(engine)
session: Session = __session()