from wtforms import Form, StringField
from wtforms.validators import DataRequired


class Kategorieform(Form):
    kategorie = StringField('kategorie', validators = [DataRequired()])

