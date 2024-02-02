from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    fullname = StringField("Your Full Name", validators=[InputRequired()])
    address = StringField("Your Address", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    submit = SubmitField("Place Your Order", render_kw={"class": "btn btn-primary"})

