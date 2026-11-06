import pytest
from app.module import app

def test_app_is_callable():
    assert callable(app)

def test_login_page_contains_form():
    content = app()
    assert "<form" in content
    assert 'name="username"' in content
    assert 'name="password"' in content
    assert 'value="Login"' in content
