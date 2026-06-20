from dotenv import load_dotenv
from dataclasses import dataclass
import os


load_dotenv()

@dataclass
class Settings():
    database_url : str



def get_settings() -> Settings:

    setting = Settings(
        database_url = os.getenv("DATABASE_URL")
    )


    return setting