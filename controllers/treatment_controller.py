from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repos.treatments_repo as treatments_repo

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route('/treatments')
def index():
    treatments = treatments_repo.select_all()
    return render_template('index.html', treatments = treatments)