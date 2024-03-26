#!/usr/bin/env python3

def connect_to_database(attempts=5, delay=5):
	"""Try to connect to the MySQL database with a retry mechanism."""
	for attempt in range(attempts):
		try:
			conn = mysql.connector.connect(
				host='mydatabase',  # Use the database name
				port=3308,  # Use the custom port
				user='root',
				password='myrootpassword',
				database='mydatabase'
			)
			return conn
		except Error as e:
			print(f"Attempt {attempt + 1}/{attempts} failed: {e}")
			time.sleep(delay)
	raise Exception("Failed to connect to the database after multiple attempts")
