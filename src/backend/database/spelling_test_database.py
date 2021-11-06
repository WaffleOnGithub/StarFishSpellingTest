"""
Edited by: Liud and Jacob
Date edited: 05/11/21

Defines connections for database
"""

import sqlite3

connection = sqlite3.connect("backend/database/spelling_test.db")  # Opens db
cursor = connection.cursor()  # Controls connection
