from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CreateProfileForm(FlaskForm):
  user_id = IntegerField('user_id', validators=[DataRequired()])
  profile_picture = StringField('profile_picture', validators=[DataRequired()])
  name = StringField('name', validators=[DataRequired()])
  age = IntegerField('age', validators=[DataRequired()])
  emergency_contacts = StringField('emergency_contacts')
  blood_type = StringField('blood_type')
  allergies = StringField('allergies')
  medical_conditions = StringField('medical_conditions')
  medications = StringField('medications')
  medication_allergies = StringField('medication_allergies')
  relatives = StringField('relatives')
  height = StringField('height')
  weight = IntegerField('weight')
  hair_color = StringField('hair_color')
  distinctive_features = StringField('distinctive_features')
  shoe_size = IntegerField('shoe_size')
  clothing_size = StringField('clothing_size')
  address = StringField('address')
