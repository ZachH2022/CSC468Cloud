CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS cattle (
    ID INT PRIMARY KEY,
    Breed VARCHAR(255),
    Weight INT,
    Age INT
);
