import pytest
from app.module import login

def test_login_success():
    assert login("alice", "wonderland") is True

def test_login_failure_wrong_password():
    assert login("alice", "wrong") is False

def test_login_failure_unknown_user():
    assert login("charlie", "chocolate") is False
