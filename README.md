# python-project

How to run the app

1. In your terminal, create a database called 'my first app'.
Run command:
```createdb myfirstapp```
2. Within the python-project file, initialise and populate database using the pythonapp.sql file.
Run command:
```psql -d myfirst app -f pythonapp.sql```
3. Run flask to open the app locally.
Run command:
```flask run```
4. Open app by opening (http://localhost:4999/) in your browser, preferably in Chrome:
<img src="screenshots/homepage.png" alt="screenshot of app home page" width="50%" height="25%">
![screenshots](Screenshot 2023-03-29 at 11.20.18)