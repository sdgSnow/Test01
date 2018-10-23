from wtforms import Form, StringField, IntegerField,validators
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[validators.DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=55)],default=1)