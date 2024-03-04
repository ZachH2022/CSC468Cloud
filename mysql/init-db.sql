CREATE TABLE IF NOT EXISTS pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    breed VARCHAR(255),
    weight INT,
    height INT
);

LOAD DATA INFILE '/docker-entrypoint-initdb.d/data.csv'
INTO TABLE pets
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(name, breed, weight, height);
