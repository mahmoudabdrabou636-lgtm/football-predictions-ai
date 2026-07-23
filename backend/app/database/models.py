from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime

from backend.app.database.connection import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)

    home_team = Column(String, nullable=False)
    away_team = Column(String, nullable=False)

    home_goals = Column(Integer)
    away_goals = Column(Integer)

    home_win_probability = Column(Float)
    draw_probability = Column(Float)
    away_win_probability = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)
