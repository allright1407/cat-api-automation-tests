import pytest
from src.api_client import CatAPIClient


@pytest.fixture(scope="session")
def api_client():
    """Fixture to initialize and provide the CatAPIClient for test functions."""
    return CatAPIClient()
