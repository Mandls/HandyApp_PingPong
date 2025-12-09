from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.matches import MatchBaseCreate, MatchesUpdate, PlayerUpdate, MatchBaseRead

import app.crud.matches as crud_matches

router = APIRouter(prefix="/matches", tags=["matches"])

stored_players = {
    "player_1": "Spieler 1",
    "player_2": "Spieler 2"
}

@router.get("/", response_model= List[MatchesUpdate])
async def get_matches():
    result = crud_matches.get_matches()
    if not result:
        raise HTTPException(status_code=404, detail="No Matches played")
    return result

@router.get("/sorted/", response_model= List[MatchBaseRead])
async def get_matches_sorted():
    result = crud_matches.get_matches_sorted()
    if not result:
        raise HTTPException(status_code=404, detail="No Matches played")
    return result

@router.post("/create_match/")
async def create_match(match: MatchBaseCreate):
    global stored_players

    # Spieler automatisch aus gespeichertem Zustand einsetzen
    match_data = match.dict()
    match_data["player_1_name"] = stored_players.get("player_1", "Player 1")
    match_data["player_2_name"] = stored_players.get("player_2", "Player 2")

    result = crud_matches.create_match(match_data)
    if not result:
        raise HTTPException(status_code=404, detail="Problem with adding")
    return result

@router.post("/settings/players")
def update_players(data: PlayerUpdate):
    global stored_players
    stored_players = data.dict()
    return {"status": "players updated", "players": stored_players}
