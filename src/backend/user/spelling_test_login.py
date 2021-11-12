"""
Edited by: Jacob
Date edited 12/11/21

All functions for logging user in
"""

from ..database import cursor, execute
from ..user.spelling_test_user_helper_functions import hash_password


def login(username, password):
    """
    Takes provided username and password and authenticates user

    :param username: username as a string
    :param password: password as a string
    :return: dictionary with success boolean and message
    """

    # Checks to see if fields are empty
    for arg in [username, password]:
        if len(arg) == 0:
            return {"success": False, "message": "Please fill in all fields"}

    statement = "SELECT password FROM Users WHERE username = ?"  # Write SQL statement to be executed
    execute(statement, (username,))
    result = cursor.fetchall()  # Gather results

    if not result:
        return {"success": False, "message": "Incorrect username or password"}

    salt = result[0][0][:32]  # Extract salt from password field as both hashed password and salt are stored in same string

    if hash_password(password, salt) == result[0][0]:  # Compare hash of input to hash in db
        return {"success": True, "message": "Success"}
    else:
        return {"success": False, "message": "Incorrect username or password"}
