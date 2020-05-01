from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email

# Will be moved to another module
class LoginForm(FlaskForm):
    username = StringField('Username ', validators = [InputRequired()])
    password = PasswordField('Password ', validators = [InputRequired()])
    remember = BooleanField('Remember Me')

