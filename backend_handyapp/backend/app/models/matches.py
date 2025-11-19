from sqlalchemy import Column, Integer, String, DateTime, func
from app.database.session import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False, default="Ping Pong Match", server_default="Ping Pong Match")
    player_1_name = Column(String(50), nullable=False, default="Player 1", server_default="Player 1")
    player_2_name = Column(String(50), nullable=False, default="Player 2", server_default="Player 2")

    score_1 = Column(Integer, nullable=False, default=0, server_default="0")
    score_2 = Column(Integer, nullable=False, default=0, server_default="0")

    status = Column(String(20), nullable=False, default="active", server_default="active")

    created_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now(), onupdate=func.now(), nullable=False)
