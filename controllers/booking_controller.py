from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repos.bookings_repo as bookings_repo

bookings_blueprint = Blueprint("bookings", __name__)

