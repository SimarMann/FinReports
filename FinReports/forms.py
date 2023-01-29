"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length, Optional)


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email address',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email address',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    
class ChangePasswordForm(FlaskForm):
    """User Change Password Form."""
    current_password = PasswordField(
        'Current Password', 
        validators=[DataRequired()]
        )
    
    new_password = PasswordField(
        'New Password', 
        validators=[DataRequired(), Length(min=6, message='Select a stronger password.')]
        )
    
    confirm_password = PasswordField(
        'Confirm New Password', 
         validators=[DataRequired(), EqualTo('new_password', message='Passwords must match.')]
         )
    
    submit = SubmitField('Change Password')
    