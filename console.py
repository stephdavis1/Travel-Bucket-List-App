import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository

import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

# _________________________________________________________

country1 = Country("Italy", "60,461,826", "Italian", "Euro", "26°C")
country_repository.save(country1)

country2 = Country("Morocco", "36,910,560", "Arabic/French", "Dirham", "36°C")
country_repository.save(country2)

country3 = Country("America", "331,000,000", "English", "Dollars", "21.5°C")
country_repository.save(country3)

country4 = Country("Germany", "83,783,942", "German", "Euro", "10.2°C")
country_repository.save(country4)

# _________________________________________________________


city_1 = City("Rome", "City Break", country1)
city_repository.save(city_1)

city_2 = City("Tangier", "Near the Sea", country2)
city_repository.save(city_2)

city_3 = City("New York", "City Break", country3)
city_repository.save(city_3)

city_4 = City("Berlin", "City Break", country4)
city_repository.save(city_4)

city_5 = City("Munich", "City Break", country4)
city_repository.save(city_5)

city_6 = City("Hamburg", "City Break", country4)
city_repository.save(city_6)

pdb.set_trace()


