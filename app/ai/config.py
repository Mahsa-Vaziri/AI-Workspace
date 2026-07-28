from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3.5-flash-lite"

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found. Add it to the .env file."
    )