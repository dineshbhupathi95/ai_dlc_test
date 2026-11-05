# Simple authentication module

USERS = {
    'alice': 'wonderland',
    'bob': 'builder',
    'charlie': 'chocolate'
}

def login(username: str, password: str) -> bool:
    '''
    Validate user credentials.

    Parameters:
        username (str): The username.
        password (str): The password.

    Returns:
        bool: True if credentials are valid, False otherwise.
    '''
    return USERS.get(username) == password

def get_user(username: str):
    '''
    Retrieve user information.

    Parameters:
        username (str): The username.

    Returns:
        dict or None: User info dict if exists, else None.
    '''
    if username in USERS:
        return {'username': username, 'password': USERS[username]}
    return None
