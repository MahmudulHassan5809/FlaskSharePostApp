from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from blog.models import User


class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Passowrd',validators=[DataRequired()])
	submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	username = StringField('UserName',validators=[DataRequired()])
	password = PasswordField('Passowrd',validators=[DataRequired(),EqualTo('pass_confirm',message='Password Must Match')])
	pass_confirm = PasswordField('Confirm Passowrd',validators=[DataRequired()])
	submit = SubmitField('Register')


	def check_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise validationError('Your Email Has Benn Registered ALready')

	def check_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise validationError('Your UserName Has Benn Registered ALready')


class UpdateuserForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	username = StringField('UserName',validators=[DataRequired()])
	picture = FileField('Update Profile Avatar',validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Update')

	def check_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise validationError('Your Email Has Benn Registered ALready')

	def check_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise validationError('Your UserName Has Benn Registered ALready')
