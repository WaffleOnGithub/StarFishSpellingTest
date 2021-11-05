"""
Edited by: Liud and Jacob
Date edited: 05/11/21

This file executes SQL commands while using prepared statements to
avoid SQL injection
"""

import sqlite3

connection = sqlite3.connect("spelling_test.db")  # Connects to db
cursor = connection.cursor()  # Controls connection


def insert(table, *args):
    """
    Inserts values into a table

    :param table: name of table as a string
    :param args: Values to be inserted
    """

    placeholder = ""  # String to be put in SQL statement as a placeholder for real values, this is to avoid SQL injection
    for i in range(0, len(args):
        if i == len(args) - 1:
            placeholder += "?, "  # ? represents a value. The placeholder string has a ? for each value being inserted
        else:
            placeholder += "?"  # makes sure no comma is added if this is the last value

    # Insert data into table. Uses f-strings which allows variables to be put inside {}
    cursor.execute(f"INSERT INTO {table} VALUES ({placeholder})", args)  #
