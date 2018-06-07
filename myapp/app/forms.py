from wtforms import Form, StringField, validators


class SearchForm(Form):
    input=StringField("")

