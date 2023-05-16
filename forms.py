from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length



class ContactForm(FlaskForm):
    name = StringField(validators=[Length(min=1, max=255)])
    email = StringField(validators=[DataRequired(), Email()])
    subject = StringField(validators=[Length(min=1)])
    message = StringField(validators=[Length(min=1)])
    submit = SubmitField('Send Message')