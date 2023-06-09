from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repos.treatments_repo as treatments_repo

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route('/treatments')
def index():
    treatments = treatments_repo.select_all()
    return render_template('treatments/index.html', treatments = treatments)

@treatments_blueprint.route('/treatments/<id>')
def show(id):
    treatment = treatments_repo.select(id)
    return render_template('treatments/show.html', treatment = treatment)