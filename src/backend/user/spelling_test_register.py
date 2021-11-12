"""
Edited by: Jacob
Date edited: 12/11/21

Registers user whilst validating users and passwords
"""

from ..database import cursor, connection, execute
from ..user.spelling_test_user_helper_functions import hash_password
import os
import re  # Used to make sure password meets requirements e.g. At least one special character


def register(username, password, email):
    """
    This function verifies the validity of the username and password and hashes it

    :param username: username as a string
    :param password: password as a string
    :param email: email as a string
    :return: returns dictionary with success boolean and message
    """

    # Checks to see if fields are empty
    for arg in [username, password, email]:
        if len(arg) == 0:
            return {"success": False, "message": "Please fill in all fields"}

    # Validates credentials and returns messages if error
    if not valid_username(username)["success"]:
        return valid_username(username)
    if not valid_password(password)["success"]:
        return valid_password(password)

    salt = os.urandom(32)  # Randomly generated salt which is used in the hashing
    storage = hash_password(password, salt)  # Hashed password combined with salt

    statement = "INSERT INTO Users VALUES (?, ?, ?)"  # Build SQL statement to insert new user into database
    execute(statement, (username, storage, email))  # Insert new user
    connection.commit()  # Save the changes

    return {"success": True, "message": "Success"}


def valid_username(username):
    """
    Helper function for register that validates username length and availability

    :returns: dictionary containing success boolean and message
    """

    if len(username) < 3:
        return {"success": False, "message": "Your username must be at least 3 characters long"}
    if len(username) > 20:
        return {"success": False, "message": "Your username cannot be longer than 20 characters"}

    # Code to count all records where username already used
    statement = "SELECT COUNT(*) FROM Users WHERE username = ?"
    # Execute statement
    execute(statement, (username,))

    result = cursor.fetchone()
    if result[0] > 0:  # Gets number of records where username already used
        return {"success": False, "message": "That username is already in use"}

    return {"success": True}  # Return success = True if requirements passed


def valid_password(password):
    """
    Helper function for register that validates password length and requirements

    :returns: dictionary containing success boolean and message
    """

    if len(password) < 5:
        return {"success": False, "message": "Your password must be at least 5 characters long"}
    if re.search("[0-9]", password) is None:
        return {"success": False, "message": "Your password must contain at least one number"}
    if re.search("[A-Z]", password) is None:
        return {"success": False, "message": "Your password must contain at least one capital letter"}
    if re.search("[$&+,:;=?@#|'<>.^*()%!]", password) is None:
        return {"success": False, "message": "Your password must contain at least one special character"}
    return {"success": True}
