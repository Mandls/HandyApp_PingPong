from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MatchBaseCreate(BaseModel):
    name: str
    player_1_name: str
    player_2_name: str
    score_1: int
    score_2: int
    status: str

class MatchesUpdate(MatchBaseCreate):
    id: int
    registered_at: datetime
    updated_at: Optional[datetime]