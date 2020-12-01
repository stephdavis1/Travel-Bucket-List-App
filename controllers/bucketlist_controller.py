from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

bucketlist_blueprint = Blueprint("bucketlist", __name__)


@bucketlist_blueprint.route("/bucketlist")
def bucketlist():

    bucketlist_cities = [city for city in city_repository.select_all() if city.visited is False]

    countries = country_repository.select_all()
    bucketlist_countries = []
    for country in countries:
        if country.visited is False:
            bucketlist_countries.append(country)

    # import pdb; pdb.set_trace()
    return render_template("/bucketlist.html", all_cities=bucketlist_cities, all_countries = bucketlist_countries)

