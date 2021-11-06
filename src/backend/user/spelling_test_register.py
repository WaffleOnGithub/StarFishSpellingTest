"""
Edited by: Jacob
Date edited: 05/11/21

Registers user whilst checking for duplicate usernames,
verifying passwords and hashing passwords
"""

from src.backend.database.spelling_test_database import cursor, connection
import os
import hashlib  # Used to hash passwords
import re  # Used to make sure password meets requirements e.g. At least one special character


def register(username: str, password: str, email: str):
    """
    This function verifies the validity of the username and password and hashes it

    :param username: username as a string
    :param password: password as a string
    :param email: email as a string
    :return: returns dictionary with success boolean and message
    """

    # Validates credentials and returns messages if error
    if not valid_username(username)["success"]:
        return valid_username(username)
    if not valid_password(password)["success"]:
        return valid_password(password)

    storage = hash_password(password)

    # Build SQL statement to insert new user into database
    statement = "INSERT INTO Users VALUES (?, ?, ?)"

    # Insert new user
    cursor.execute(statement, (username, storage, email))

    # Save the changes
    connection.commit()

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
    statement = "SELECT COUNT (*) FROM Users WHERE username = ?"
    # Execute statement
    cursor.execute(statement, [username])

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

def hash_password(password):
    """
    Helper function for register that hashes a password

    :returns: hashed key with salt
    """

    # Randomly generated salt which is used in the hashing
    salt = os.urandom(32)

    # Hashes password
    key = hashlib.pbkdf2_hmac(
        "sha256",  # Hash digest algorithm
        password.encode("utf-8"),  # Convert password to bytes
        salt,
        100000  # Iterations of hash digest algorithm
    )

    # Return salt and hashed password together
    return salt + key
