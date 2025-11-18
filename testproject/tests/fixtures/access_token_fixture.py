import pytest
from elrahapi.authentication.token import TokenType

from ...testproject.main import authentication


@pytest.fixture
def access_token_fixture():
    access_token = authentication.create_token(
        data={"sub": "test"}, token_type=TokenType.ACCESS_TOKEN
    )
    return access_token


@pytest.fixture
def refresh_token_fixture():
    refresh_token = authentication.create_token(
        data={"sub": "test"}, token_type=TokenType.REFRESH_TOKEN
    )
    return refresh_token
