import pytest
from fastapi.testclient import TestClient

from ...testproject.main import app



@pytest.fixture
def client():
    client = TestClient(app)
    yield client
