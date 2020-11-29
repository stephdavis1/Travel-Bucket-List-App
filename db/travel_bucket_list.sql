DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    population VARCHAR (255),
    language_spoken VARCHAR(255),
    currency_used VARCHAR (255),
    average_temperature VARCHAR (255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_type VARCHAR(255),
    countries_id INT REFERENCES countries(id)
);