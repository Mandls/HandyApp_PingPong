from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.matches import MatchBaseCreate, MatchesUpdate

import app.crud.matches as crud_matches

router = APIRouter(prefix="/matches", tags=["matches"])

@router.get("/", response_model= List[MatchesUpdate])
async def get_matches():
    result = crud_matches.get_matches()
    if not result:
        raise HTTPException(status_code=404, detail="No Matches played")
    return result

@router.get("/sorted/", response_model= List[MatchesUpdate])
async def get_matches_sorted():
    result = crud_matches.get_matches_sorted()
    if not result:
        raise HTTPException(status_code=404, detail="No Matches played")
    return result

@router.post("/create_match/")
async def create_match(match: MatchBaseCreate):
    result = crud_matches.create_match(match=match)
    if not result:
        raise HTTPException(status_code=404, detail="Problem with adding")
    return result
