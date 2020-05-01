from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from datetime import datetime
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'thisShouldBeChanged!!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/aaronabraham/Documents/Programming/Python/COVID-19-Website/database.db' # This needs to be changed as well
db = SQLAlchemy(app)

# Creating database class. This will need to be moved to a separate module later
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(), unique = True)
    email = db.Column(db.String(), unique = True)
    password = db.Column(db.String())

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/donate')
def donate():
    return render_template('donation.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user:
           if user.password = form.password.data:
                return redirect(url_for('dashboard')) # This is to create new resources
        else:
            return '<h1> Invalid username or password </h1>'

    return render_template('login.html', form = form)

# Making debugging and development easier (hot reload). Must remove when going to prod
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)