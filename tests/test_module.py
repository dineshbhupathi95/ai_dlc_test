import pytest
from app.module import login, get_user

def test_login_success():
    assert login('alice', 'wonderland') is True

def test_login_failure_wrong_password():
    assert login('alice', 'wrong') is False

def test_login_failure_unknown_user():
    assert login('unknown', 'pass') is False

def test_get_user_exists():
    user = get_user('bob')
    assert user == {'username': 'bob', 'password': 'builder'}

def test_get_user_not_exists():
    assert get_user('unknown') is None
