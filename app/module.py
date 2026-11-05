USERS = {"alice": "wonderland", "bob": "builder"}

def login(username, password):
    """Return True if username and password match known users."""
    return USERS.get(username) == password

def get_login_page():
    """Return a simple representation of a login page."""
    return "Login Page"
