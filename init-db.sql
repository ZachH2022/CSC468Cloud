-- Create a new database
CREATE DATABASE CattleDB;
USE CattleDB;

-- Create a table to store the data
CREATE TABLE Cattle (
    Name VARCHAR(50),
    Breed VARCHAR(50),
    WeightKG INT,
    HeightCM INT,
    Description VARCHAR(MAX)
);

-- Import data from the CSV file
BULK INSERT Cattle
FROM '/cattle.csv'
WITH (
    FIELDTERMINATOR = ',',  -- CSV field delimiter
    ROWTERMINATOR = '\n',   -- CSV row delimiter
    FIRSTROW = 2            -- Skip the header row
);
