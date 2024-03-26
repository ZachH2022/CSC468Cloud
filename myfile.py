#!/usr/bin/env python3
import time
import pandas as pd
import mysql.connector
from mysql.connector import Error

def connect_to_database(attempts=5, delay=5):
	"""Try to connect to the MySQL database with a retry mechanism."""
	for attempt in range(attempts):
		try:
			conn = mysql.connector.connect(
				host='localhost',
				user='root',
				password='myrootpassword',
				database='mydatabase'
			)
			return conn
		except Error as e:
			print(f"Attempt {attempt + 1}/{attempts} failed: {e}")
			time.sleep(delay)
	raise Exception("Failed to connect to the database after multiple attempts")
	
# Read the CSV file into a DataFrame
df = pd.read_csv('/tmp/cattle.csv')

# Connect to the MySQL database
conn = connect_to_database()

cursor = conn.cursor()

# Insert the data into the database
for i, row in df.iterrows():
	sql = "INSERT INTO cattle (ID, Breed, Weight, Age) VALUES (%s, %s, %s, %s)"
	cursor.execute(sql, tuple(row))
	conn.commit()
	
# Close the connection
cursor.close()
conn.close()
