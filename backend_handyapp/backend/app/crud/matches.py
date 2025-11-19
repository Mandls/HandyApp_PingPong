from app.core.supabase import supabase
from app.schemas.matches import MatchBaseCreate, MatchesUpdate
from datetime import datetime, timedelta

def get_matches():
    response = supabase.table("matches").select("*").execute()
    return response.data

def create_match(match: MatchBaseCreate):
    response = supabase.table("matches").insert(match.dict()).execute()
    return response.data[0] if response.data else None
