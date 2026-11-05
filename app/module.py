"""Simple login module."""

# In-memory user store
USERS = {
    "alice": "wonderland",
    "bob": "builder",
}

def login(username: str, password: str) -> bool:
    """
    Validate username and password against the USERS store.
    Returns True if credentials match, False otherwise.
    """
    return USERS.get(username) == password
