from flask import Flask, render_template

from controllers.bookings_controller import bookings_blueprint 
from controllers.treatments_controller import treatments_blueprint 


app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(treatments_blueprint)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
