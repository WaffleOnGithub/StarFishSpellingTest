"""
Edited by: Liud and Jacob
Date edited: 05/11/21

Init file for backend package
"""
import sqlite3

connection = sqlite3.connect("spelling_test.db")
cursor = connection.cursor()


def insert(table, *args):
    print(args)  # Insert data into table
