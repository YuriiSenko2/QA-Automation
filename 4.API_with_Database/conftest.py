import pytest

from API_with_Database.repo.store_repo import StoreRepo


@pytest.fixture
def db_and_api():
    yield StoreRepo()
