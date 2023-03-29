# python-project

The brief

I have created a treatment booking app where a user can book treatments at a nail bar. It is assumed the user is already signed in and are accessing their own portal. A customer should be able to create a Booking with a name, date, time, and Treatment. A customer should be able to see all their scheduled treatments and click through on one to edit it or cancel it.

How to run the app

1. In your terminal, create a database called 'myfirstapp'. Run command: ```createdb myfirstapp```

2. Within the python-project file, initialise and populate database using the pythonapp.sql file. Run command: ```psql -d myfirst app -f pythonapp.sql```

3. Run flask to open the app locally. Run command: ```flask run```

4. Open app by opening (http://localhost:4999/) in your browser, preferably in Chrome:
<img src="screenshots/homepage.png" alt="screenshot of app home page" height="50%">

5. Use the app to view all available treatments by clicking on 'Our Treatments' from the navigation menu:
<img src="screenshots/treatments.png" alt="screenshot of treatment list page" height="50%">

6. Click into each treatment for more information. 

7. Click 'Book' from the individual treatment page or 'Book Now' from the navigation buttons to be taken to a booking form:
<img src="screenshots/bookingform.png" alt="screenshot of booking page" height="50%">

8. To view all bookings made, click on 'My Bookings':
<img src="screenshots/bookings.png" alt="screenshot of all bookings page" height="50%">

9. Here you have the option to amend or cancel your booking. 

10. To exit the app, end flask. Run command: ```ctrl c```

View presentation here: https://docs.google.com/presentation/d/1JXYMAtcFsIuy5XqlLiimWVVVQSffDHdO1wZpN2FYQJU/edit?usp=sharing