from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository



# create
def save(city):
    sql = "INSERT INTO cities (name, city_type, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.city_type, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id



# read - select all
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["country_id"])
        city = City(row['name'], row['city_type'], country, row['id'])
        cities.append(city)
    return cities



# read - select one
def select(id):
    city = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['title'], result['city_type'], country, result['id'])
    return city



# delete - delete one
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)



# delete - delete all
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)



# update city
def update(city):
    sql = "UPDATE cities SET (name, city_type, country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.city_type, city.country.id, city.id]
    print(values)
    run_sql(sql, values)