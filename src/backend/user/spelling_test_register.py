"""

"""

from ..database import insert


def register(username: str, password: str, email: str):
    """
    This function verifies the validity of the username and password and hashes it

    :param username: username as a string
    :param password: password as a string
    :param email: email as a string
    :return: true on success or error message on fail
    """

    if not valid_username(username):
        return
    insert("Users", username, password, email)

def valid_username(username):
    pass

def valid_password(password):
    pass
