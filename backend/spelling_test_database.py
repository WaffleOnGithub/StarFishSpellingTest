import sqlite3

connection = sqlite3.connect("spelling_test.db")

cursor = connection.cursor()

def insert():