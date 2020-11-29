from db.run_sql import run_sql

from models.country import Country

#create
def save(country_to_save):
    sql = "INSERT INTO countries(self, name, population, language_spoken, currency_used, average_temp) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [country_to_save.name, country_to_save.population, country_to_save.language_spoken, country_to_save.currency_used, country_to_save.average_temp]
    sql_results = run_sql(sql, values)
    country_to_save.id = sql_results[0]['id']
    return country_to_save


#read - select all

#read - select one

#delete - delete one

#delete - delete all

#update one

