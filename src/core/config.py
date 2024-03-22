from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DATABASE_URL = (
    f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

SECRET_AUTH = os.environ.get("SECRET_AUTH")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://langcards.fun",
    "https://langcards.fun",
    "https://blenemy.github.io/chess-app/",
]
