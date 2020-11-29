import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

italy = Country("Italy", 60461826, "Italian", "Euro", "26°C")
country_repository.save(italy)


morocco = Country("Morocco", 36910560, "Arabic", "Dirham", "36°C")
country_repository.save(morocco)

pdb.set_trace()