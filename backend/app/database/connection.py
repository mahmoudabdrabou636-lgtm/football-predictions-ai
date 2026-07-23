import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Read DATABASE_URL from environment variable with fallback for local development
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://fpai_user:fpai_password@database:5432/football_predictions"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
