from app.core.supabase import supabase
from app.schemas.matches import MatchBaseCreate, MatchesUpdate, MatchBaseRead
from datetime import datetime, timedelta

def get_matches():
    response = supabase.table("matches").select("*").execute()
    return response.data

def get_matches_sorted():
    response = (
        supabase
        .table("matches")
        .select("*")
        .execute()
    )
    
    matches = response.data
    
    # sortiere nach dem größeren der beiden Scores
    matches.sort(key=lambda m: max(m["score_1"], m["score_2"]), reverse=True)
    
    return matches

def create_match(match_data: dict):
    response = supabase.table("matches").insert(match_data).execute()
    return response.data[0] if response.data else None
