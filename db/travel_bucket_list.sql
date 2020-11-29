DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    language VARCHAR (255),
    population INT
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    population INT
    countries_id INT REFERENCES countries(id)
);