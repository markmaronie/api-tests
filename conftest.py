import pytest

from src.api.api_client import ApiClient
from src.assertions.assertion_base import Asserts


@pytest.fixture(scope="session")
def base_client():
    """Создаем фиксутуру клиента"""
    client = ApiClient()

    return client


@pytest.fixture(scope="session")
def base_asserts():
    """Создаем фиксутуру ассертов"""
    asserts = Asserts()

    return asserts