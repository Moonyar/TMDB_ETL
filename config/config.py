import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    raise ValueError("No API key found.")
