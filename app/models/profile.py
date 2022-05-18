from .db import db

class Profile(db.Model):
  __tablename__ = 'profiles'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, nullable=False, unique=True)
  profile_picture = db.Column(db.String(500), nullable=True)
  name = db.Column(db.String(500), nullable=False)
  phone_number = db.Column(db.String)
  # birth_date = db.Column(db.Date, nullabe=False)
  age = db.Column(db.Integer, nullable=False)
  # # # emergency_contacts
  blood_type = db.Column(db.String, nullable=True)
  allergies = db.Column(db.String, nullable=True)
  medical_conditions = db.Column(db.String, nullable=True)
  medications = db.Column(db.String, nullable=True)
  medication_allergies = db.Column(db.String, nullable=True)
  height = db.Column(db.String, nullable=True)
  weight = db.Column(db.Integer, nullable=True)
  hair_color = db.Column(db.String, nullable=True)
  distinctive_features = db.Column(db.String, nullable=True)
  shoe_size = db.Column(db.Integer, nullable=True)
  clothing_size = db.Column(db.String, nullable=True)
  address = db.Column(db.String, nullable=True)

  def to_dict(self):
            return {
                'id': self.id,
                'user_id': self.user_id,
                'profile_picture' : self.profile_picture,
                'name': self.name,
                'phone_number': self.phone_number,
                'age': self.age,
                'blood_type': self.blood_type,
                'allergies' : self.allergies,
                'medical_conditions': self.medical_conditions,
                'medications': self.medications,
                'medication_allergies': self.medication_allergies,
                'height': self.height,
                'weight': self.weight,
                'hair_color': self.hair_color,
                'distinctive_features': self.distinctive_features,
                'shoe_size': self.shoe_size,
                'clothing_size': self.clothing_size,
                'address': self.address
            }

