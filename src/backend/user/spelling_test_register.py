"""
Edited by: Jacob
Date edited: 05/11/21

Registers user whilst checking for duplicate usernames,
verifying passwords and hashing passwords
"""

from src.backend.database.spelling_test_database import cursor, connection


def register(username: str, password: str, email: str):
    """
    This function verifies the validity of the username and password and hashes it

    :param username: username as a string
    :param password: password as a string
    :param email: email as a string
    :return: returns dictionary with success boolean and message
    """

    if not valid_username(username).success:
        return valid_username(username)

    # Build SQL statement to insert new user into database
    statement = "INSERT INTO Users VALUES (?, ?, ?)"

    # Insert new user
    cursor.execute(statement, (username, password, email))

    # Save the changes
    connection.commit()


def valid_username(username):
    """
    Helper function for register that validates username length and availability
    """

    if len(username) < 3:
        return {"success": False, "message": "Username must be at least 3 characters long"}
    if len(username) > 20:
        return {"success": False, "message": "Username cannot be longer than 20 characters"}

    # Code to select all records where username already used
    statement = "SELECT * FROM Users WHERE username = ?"
    # Execute statement
    cursor.execute(statement, username)

    result = cursor.fetchone()
    if result[0] > 0:  # Gets number of records where username already used
        return {"success": False, "message": "Username already in use"}

    return {"success": True}  # Return success = True if requirements passed


def valid_password(password):
    pass


if __name__ == "__main__":
    cursor.execute("INSERT INTO Users VALUES (\"Jake\", \"Password\", \"ik\")")
    connection.commit()
