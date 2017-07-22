from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import *


class SignupForm(Form):
    name = TextField(u'Your name', validators=[Required()])
    fileHandler = FileField(u'File:', validators=[Required()])
    keys = TextField(u'Keywords (seperated by ,)', validators=[])
    submit = SubmitField(u'Save')
