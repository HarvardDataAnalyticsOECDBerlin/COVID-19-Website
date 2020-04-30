from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email

# Will be moved to another module
class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired()])
    password = PasswordField('password', validators = [InputRequired()])
    remember = BooleanField('remember')

