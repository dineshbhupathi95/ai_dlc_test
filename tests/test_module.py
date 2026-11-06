import pytest
from app.module import app

def test_app_is_callable():
    assert callable(app)

def test_login_page_contains_form():
    content = app()
    assert "<!DOCTYPE html>" in content
    assert "<title>Login</title>" in content
    assert "<h1>Login</h1>" in content
    assert '<form action="/login" method="post">' in content
    assert 'name="username"' in content
    assert 'name="password"' in content
    assert 'value="Login"' in content
