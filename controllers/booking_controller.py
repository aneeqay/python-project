from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repos.bookings_repo as bookings_repo
import repos.treatments_repo as treatments_repo
from models.booking import Booking

bookings_blueprint = Blueprint("bookings", __name__)

# @bookings_blueprint.route('/treatments', methods=['POST'])
# def add_to_basket():
#     return

# read
@bookings_blueprint.route('/bookings')
def show_all():
    bookings = bookings_repo.select_all()
    return render_template('bookings/index.html', bookings = bookings)

@bookings_blueprint.route('/bookings', methods=['POST'])
def create_booking():
    date = request.form['date']
    time = request.form['time']
    treatment_id = request.form['treatments']
    treatment = treatments_repo.select(treatment_id)
    booking = Booking(date, time, treatment)
    bookings_repo.save(booking)
    my_booking = bookings_repo.select(booking.id)
    return render_template('bookings/confirmation.html', booking = my_booking)

# read
@bookings_blueprint.route("/bookings/<id>")
def show_booking(id):
    booking = bookings_repo.select(id)
    return render_template('bookings/show.html', booking = booking)

@bookings_blueprint.route("/bookings/new")
def new_booking():
    treatments = treatments_repo.select_all()
    return render_template('bookings/new.html', treatments = treatments)

@bookings_blueprint.route('/bookings/<id>/edit')
def update(booking):
    pass


@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete(id):
    pass