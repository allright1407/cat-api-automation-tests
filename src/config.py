import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file


class Config:
    CAT_API_KEY = os.getenv('CAT_API_KEY')
    CAT_API_URL = os.getenv('CAT_API_URL',
                            'https://api.thecatapi.com/v1')  # Default to https://api.thecatapi.com/v1 if not set
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')  # Default to INFO if not set

    @classmethod
    def validate(cls):
        if not cls.CAT_API_KEY:
            raise ValueError("CAT_API_KEY is required for authentication.")
