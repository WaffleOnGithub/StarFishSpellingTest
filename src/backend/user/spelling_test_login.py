"""
Edited by: Jacob
Date edited 07/11/21

All functions for logging user in
"""

from ..database import cursor, execute


def login(username: str, password: str):
    """
    Takes provided username and password and authenticates user

    :param username: username as a string
    :param password: password as a string
    :return: dictionary with success boolean adn message
    """

    statement = "SELECT password FROM Users WHERE username = ?"

    execute(statement, (username,))

    if cursor.fetchone()[0] == 0:
        return {"success": False, "message": "incorrect username or password"}
