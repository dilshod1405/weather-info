import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if OPENWEATHER_API_KEY is None:
    raise ValueError("OPENWEATHER_API_KEY is not set")

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY is not set")

OPENWEATHER_API_URL = os.getenv("OPENWEATHER_API_URL")