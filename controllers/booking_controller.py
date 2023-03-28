from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repos.bookings_repo as bookings_repo
import repos.treatments_repo as treatments_repo
from models.booking import Booking

bookings_blueprint = Blueprint("bookings", __name__)

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

@bookings_blueprint.route("/bookings/<id>")
def show_booking(id):
    booking = bookings_repo.select(id)
    return render_template('bookings/show.html', booking = booking)

@bookings_blueprint.route("/bookings/new")
def new_booking():
    treatments = treatments_repo.select_all()
    return render_template('bookings/new.html', treatments = treatments)

@bookings_blueprint.route('/bookings/<id>/edit')
def amend(id):
    booking = bookings_repo.select(id)
    treatments = treatments_repo.select_all()
    return render_template('bookings/edit.html', booking = booking, treatments = treatments)

@bookings_blueprint.route('/bookings/<id>/edit', methods=['POST'])
def update(id):
    date = request.form['date']
    time = request.form['time']
    treatment_id = request.form['treatments']
    treatment = treatments_repo.select(treatment_id)
    booking = Booking(date, time, treatment, id)
    bookings_repo.update(booking)
    my_booking = bookings_repo.select(id)
    return redirect('bookings/confirmation.html', booking = my_booking)

@bookings_blueprint.route("/bookings/<id>/delete")
def confirm_delete(id):
    booking = bookings_repo.select(id)
    return render_template('bookings/delete.html', booking = booking)

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete(id):
    bookings_repo.delete(id)
    return render_template('bookings/deleted.html')