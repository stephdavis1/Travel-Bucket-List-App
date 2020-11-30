class Country:
    def __init__(self, name, population, language_spoken, currency_used, average_temperature, id=None):
        self.name = name
        self.population = population
        self.language_spoken = language_spoken
        self.currency_used = currency_used
        self.average_temperature = average_temperature
        self.id = id