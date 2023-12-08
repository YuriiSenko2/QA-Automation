import pytest

from API_testing.infrastructure.requests_structure import GetRequests
from API_testing.infrastructure.requests_structure import PostPutPatchDeleteRequests


@pytest.fixture
def get():
    yield GetRequests()


@pytest.fixture
def modifications():
    yield PostPutPatchDeleteRequests()
