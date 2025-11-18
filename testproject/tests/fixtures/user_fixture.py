import pytest


@pytest.fixture
def fake_user():
    return {
        "password": "m*td*pa**e",
        "email": "user@example.com",
        "username": "Harlequelrah",
        "lastname": "SMITH",
        "firstname": "jean-francois",
    }


@pytest.fixture
def expected_user_value():
    return {
        "date_deleted": None,
        "is_deleted": False,
        "id": 1,
        "is_active": True,
        "attempt_login": 0,
        "user_roles": [],
        "user_privileges": [],
        "email": "user@example.com",
        "username": "Harlequelrah",
        "lastname": "SMITH",
        "firstname": "jean-francois",
    }


@pytest.fixture
def fake_update_user():
    return {
        "email": "user_updated@example.com",
        "username": "testupdate",
        "lastname": "UPDATE",
        "firstname": "jean-update",
    }


# @pytest.fixture
# def expected_user_value():
#     return {
#         "date_deleted": None,
#         "is_deleted": False,
#         "id": 1,
#         "is_active": True,
#         "attempt_login": 0,
#         "user_roles": [],
#         "user_privileges": [],
#         "email": "user@example.com",
#         "username": "Harlequelrah",
#         "lastname": "SMITH",
#         "firstname": "jean-francois",
#     }
