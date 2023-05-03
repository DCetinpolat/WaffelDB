DROP DATABASE IF EXISTS waffles;
CREATE DATABASE waffles;

USE waffles;


CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    anzahl INT,
    preis INT,
    uhrzeit VARCHAR(255),
    status VARCHAR(255),
    abgeholt BOOLEAN,
    storniert BOOLEAN
);

SELECT * FROM orders;