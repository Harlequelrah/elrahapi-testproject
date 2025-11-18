import pytest
from fastapi.testclient import TestClient

from ...testproject.main import app

# from testproject.testproject.settings.database import database


# from .database_fixture import test_database


@pytest.fixture
def client():
    client = TestClient(app)
    yield client
