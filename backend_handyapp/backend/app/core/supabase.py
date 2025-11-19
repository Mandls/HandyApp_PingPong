from supabase import create_client
import os

SUPABASE_URL ='https://uvpwbjzxbnpyucyxknkb.supabase.co' #os.getenv("SUPABASE_URL")
SUPABASE_KEY ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV2cHdianp4Ym5weXVjeXhrbmtiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM0MjMzNTMsImV4cCI6MjA3ODk5OTM1M30.si3G5rFmFbAEOEpvP3kmNtA76YyuCJYPlq2sT0gBFNc' #os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
