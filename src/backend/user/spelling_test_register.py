"""
Edited by: Jacob
Date edited: 05/11/21

Registers user whilst checking for duplicate usernames,
verifying passwords and hashing passwords
"""

from ..database.spelling_test_database import cursor


def register(username: str, password: str, email: str):
    """
    This function verifies the validity of the username and password and hashes it

    :param username: username as a string
    :param password: password as a string
    :param email: email as a string
    :return: returns dictionary with success boolean and message
    """

    if not valid_username(username).success:
        return

    # Build SQL statement to insert new user into database
    statement = "INSERT INTO Users VALUES (?, ?, ?)"

    # Insert new user
    cursor.execute(statement, (username, password, email))

    # Save the changes
    cursor.commit()

def valid_username(username):
    # Code to select
    if len(username) < 3:
        return {"success": False, "message": "Username is too short"}
    statement = "SELECT * FROM Users WHERE username = ?"



def valid_password(password):
    pass
