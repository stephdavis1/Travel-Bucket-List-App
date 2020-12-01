from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

bucketlist_blueprint = Blueprint("bucketlist", __name__)


@bucketlist_blueprint.route("/bucketlist")
def bucketlist():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("/bucketlist.html", all_cities=cities, all_countries = countries)

