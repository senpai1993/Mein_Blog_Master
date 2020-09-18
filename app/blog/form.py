from wtforms import Form, StringField, DateField, IntegerField
from wtforms.validators import DataRequired



class Blogform(Form):
    title = StringField('Titel', validators = [DataRequired()])
    category = IntegerField('Kategorie', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    date = DateField('Datum', validators=[DataRequired()])

