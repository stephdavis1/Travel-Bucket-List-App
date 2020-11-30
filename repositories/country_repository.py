from db.run_sql import run_sql

from models.country import Country
from models.city import City


# create
def save(country):
    sql = "INSERT INTO countries (name, population, language_spoken, currency_used, average_temperature) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [
        country.name,
        country.population,
        country.language_spoken,
        country.currency_used,
        country.average_temperature
    ]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


# read - select all
def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(
            row["name"],
            row["population"],
            row["language_spoken"],
            row["currency_used"],
            row["average_temperature"],
            row['id']
        )
        countries.append(country)
    return countries


# read - select one
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(
            result["name"],
            result["population"],
            result["language_spoken"],
            result["currency_used"],
            result["average_temperature"],
            result["id"],
        )
    return country


# delete - delete one
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# delete - delete all
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


# update country
def update(country):
    sql = "UPDATE countries SET (name, population, language_spoken, currency_used, average_temperature) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = values = [
        country.name,
        country.population,
        country.language_spoken,
        country.currency_used,
        country.average_temperature,
        country.id,
    ]
    run_sql(sql, values)


def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['title'], row['city_type'],row['country_id'],row['id'])
        cities.append(city)
    return cities
