from flask import Flask, render_template

from controllers.booking_controller import bookings_blueprint 


app = Flask(__name__)

app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
