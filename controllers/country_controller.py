from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries/show")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)


# NEW
# GET '/countries/new'
@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    cities = city_repository.select_all()
    return render_template("countries/new.html", all_cities=cities)



# CREATE
# POST '/countries'
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    population = request.form["population"]
    language_spoken = request.form["language_spoken"]
    currency_used = request.form["currency_used"]
    average_temperature = request.form["average_temperature"]
    country = Country(name, population, language_spoken, currency_used, average_temperature)
    country_repository.save(country)
    return redirect("/countries")


# SHOW
# GET '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template("cities/show.html", country=country)


# EDIT
# GET '/countries/<id>/edit'
@countries_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_cities(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", city=city, all_countries=countries)


# UPDATE
# PUT '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    population = request.form["population"]
    language_spoken = request.form["language_spoken"]
    currency_used = request.form["currency_used"]
    average_temperature = request.form["average_temperature"]
    country = Country(name, population, language_spoken,currency_used, average_temperature, id)
    print(country.name())
    country_repository.update(country)
    return redirect("/countries")


# DELETE
# DELETE '/countries/<id>'
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")
