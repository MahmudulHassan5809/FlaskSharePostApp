from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
#from wtforms import ValidationError
#from flask_wtf.file import FileField, FileAllowed


class BlogPostForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	text  = TextAreaField('Body',validators=[DataRequired()])
	submit = SubmitField("Published Post")
