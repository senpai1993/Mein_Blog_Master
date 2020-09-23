from wtforms import Form, StringField, IntegerField, DateField
from wtforms.validators import DataRequired


class Kategorieform(Form):
    kategorie = StringField('kategorie', validators = [DataRequired()])



