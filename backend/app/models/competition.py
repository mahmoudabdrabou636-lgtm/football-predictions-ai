from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from backend.app.database import Base


class Competition(Base):
    __tablename__ = "competitions"

    competition_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(100),
        nullable=False
    )

    country = Column(
        String(100),
        nullable=False
    )

    season = Column(
        String(20),
        nullable=False
    )

    competition_type = Column(
        String(50),
        nullable=False
    )
