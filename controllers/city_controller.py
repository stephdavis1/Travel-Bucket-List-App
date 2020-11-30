from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)


@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities=cities)


# NEW
# GET '/cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries=countries)


# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form["name"]
    city_type = request.form["city_type"]
    country = country_repository.select(request.form["country_id"])
    city = City(name, city_type, country)
    city_repository.save(city)
    return redirect("/cities")


# SHOW
# GET '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template ("books/show.html", city = city)


# EDIT
# GET '/cities/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_cities(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", city = city, all_countries = countries)

# UPDATE
# PUT '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form["name"]
    city_type = request.form["city_type"]
    country = country_repository.select(request.form["country_id"])
    city = City (name, city_type, country, id)
    print(city.country.name())
    city_repository.update(city)
    return redirect('/books')

# DELETE
# DELETE '/books/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')   







    # self, name, city_type, country, id=None