import requests
import logging
from src.config import Config

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(level=Config.LOG_LEVEL)


class CatAPIClient:
    def __init__(self):
        Config.validate()
        self.base_url = Config.CAT_API_URL
        self.headers = {'x-api-key': Config.CAT_API_KEY}

    def get_images(self, params=None):
        url = f"{self.base_url}/images/search"
        logger.info(f"Requesting images with URL: {url} and params: {params}")
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        logger.debug(f"Images response: {response.json()}")
        return response.json()
