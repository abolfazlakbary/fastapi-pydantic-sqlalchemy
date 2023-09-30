from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database+library://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://admin:admin123456654321@localhost:3306/movie_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # the sessionmaker() function is a factory that creates Session objects
Base = declarative_base()

