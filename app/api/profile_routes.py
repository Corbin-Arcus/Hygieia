from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import Profile, User, db

profile_routes = Blueprint('profiles', __name__)

@profile_routes.route('/')
def test():
  return {'message' : 'Testing Testing 1...2...3...'}

@profile_routes.route('/new')
def create_profile():
  form = CreateProfileForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    profile_picture = form.data['profile_picture']
    name = form.data['name']
    age = form.data['age']
    emergency_contacts = form.data['emergency_contacts']
    blood_type = form.data['blood_type']
    allergies = form.data['allergies']
    medical_conditions = form.data['medical_conditions']
    medications = form.data['medications']
    medication_allergies = form.data['medication_allergies']
    relatives = form.data['relatives']
    height = form.data['height']
    weight = form.data['weight']
    hair_color = form.data['hair_color']
    distinctive_features = form.data['distinctive_features']
    shoe_size = form.data['shoe_size']
    clothing_size = form.data['clothing_size']
    address = form.data['address']


    new_profile = Profile(profile_picture=profile_picture, name=name, age=age, emergency_contacts=emergency_contacts, blood_type=blood_type, allergies=allergies,
    medical_conditions=medical_conditions, medications=medications, medication_allergies=medication_allergies,
    relatives=relatives, height=height, weight=weight, hair_color=hair_color, distinctive_features=distinctive_features,
    shoe_size=shoe_size, clothing_size=clothing_size, address=address)
    db.session.add(new_profile)
    db.session.commit()
    return new_profile.to_dict()

# @profile_routes.route('/<int:id>')
# def profile(id):
#   user = User.query.get(id)
#   return user.to_dict()
