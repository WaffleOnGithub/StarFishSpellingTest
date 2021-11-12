"""
Edited by: Liud and Jacob
Date edited: 12/11/21

Defines connections for database
"""

#import mysql.connector

# Opens remote db
"""connection = mysql.connector.connect(
    host="nettlecoding.co.uk",
    port="3306",
    user="spelling_test",
    password="zAsHCuL(G!FWEtRF",
    database="spelling_test"
)"""

import sqlite3

connection = sqlite3.connect("backend/database/spelling_test.db")  # Opens local db

cursor = connection.cursor()  # Controls connection

def execute(statement, values):
    cursor.execute(statement, values)