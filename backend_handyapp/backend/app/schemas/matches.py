from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MatchBaseRead(BaseModel):
    name: str
    player_1_name: str
    player_2_name: str
    score_1: int
    score_2: int

class MatchBaseCreate(BaseModel):
    score_1: int
    score_2: int

class MatchesUpdate(MatchBaseCreate):
    id: int
    registered_at: datetime

class PlayerUpdate(BaseModel):
    player_1: str
    player_2: str