from app import module

def test_login_success():
    assert module.login("alice", "wonderland") is True

def test_login_failure_wrong_password():
    assert module.login("alice", "wrong") is False

def test_login_failure_unknown_user():
    assert module.login("charlie", "anything") is False

def test_get_login_page():
    assert module.get_login_page() == "Login Page"
