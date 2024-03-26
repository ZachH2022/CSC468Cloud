# Use the official MySQL image as the base
FROM mysql:latest

# Set environment variables for MySQL
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_ROOT_PASSWORD=myrootpassword

# Copy the SQL script and CSV file into the container
COPY init-db.sql /docker-entrypoint-initdb.d/
COPY cattle.csv /tmp/cattle.csv

# Install Python and necessary libraries
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pandas mysql-connector-python

# Copy the Python script to populate the database from the CSV file
COPY populate_db.py /tmp/

# Run the Python script to populate the database
RUN python3 /tmp/populate_db.py
