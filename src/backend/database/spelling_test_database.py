"""
Edited by: Liud and Jacob
Date edited: 05/11/21

Defines connections for database
"""

import sqlite3

connection = sqlite3.connect("spelling_test.db")  # Connects to db
cursor = connection.cursor()  # Controls connection
