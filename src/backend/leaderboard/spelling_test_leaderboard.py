"""
Edited by: Jacob
Date edited: 12/11/21

Functions and procedures for getting users' leaderboard data
"""

from ..database.spelling_test_database import cursor, connection, execute


def get_data(username=None):
    """
    Function that reads leaderboard from db and returns as multi-dimensional array.
    This can be used to get a single players high score or the entire leaderboard

    :param username: username as a string
    :return: user data in the form of a multi-dimensional array
    """

    # Set SQL statement and execute, dependent on whether specific user requested or not
    if username is None:
        statement = "SELECT * FROM Leaderboard"
        execute(statement)
    else:
        statement = "SELECT * FROM Leaderboard WHERE username = ?"
        execute(statement, (username,))

    return cursor.fetchall()  # Return data


def save_data(username, score):
    """
    Procedure that updates leaderboard but only if score is bigger than saved score

    :param username: username as a string
    :param score: score as an integer
    """

    if not in_leaderboard(username):
        statement = f"INSERT INTO Leaderboard VALUES (?, {score})"  # Insert new record
    elif get_data(username)[0][1] < score:  # Gets score currently in db and checks whether new score bigger
        statement = f"UPDATE Leaderboard SET score = {score} WHERE username = ?"  # Update existing record
    else:
        return

    execute(statement, (username,))  # Execute statements
    connection.commit()  # Save changes


def in_leaderboard(username):
    """
    Helper function for save_data that checks to see if user already
    has a record in the leaderboard table or not.

    :param username: username as a string
    :return: Boolean for whether user already has a record
    """

    statement = "SELECT COUNT(*) FROM Leaderboard WHERE username = ?"  # Statement to find if user in leaderboard table
    execute(statement, (username,))

    return cursor.fetchone()[0] > 0  # Returns True if records are found for user
