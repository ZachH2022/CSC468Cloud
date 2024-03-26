import pandas as pd
import mysql.connector

# Read the CSV file into a DataFrame
df = pd.read_csv('/tmp/cattle.csv')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='myrootpassword',
    database='mydatabase'
)
cursor = conn.cursor()

# Insert the data into the database
for i, row in df.iterrows():
    sql = "INSERT INTO cattle (ID, Breed, Weight, Age) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))
    conn.commit()

# Close the connection
cursor.close()
conn.close()
