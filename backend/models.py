from config import db

class Info(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(80), unique=False, nullable=False)
     adress = db.Column(db.String(100), unique=False, nullable=False)
     dob = db.Column(db.String(80), unique=False, nullable=False)
     cin = db.Column(db.String(80), unique=False, nullable=False)
     def to_json(self):
          return {
               "id":self.id,
               "Name":self.name,
               "Adress":self.adress,
               "Dob":self.dob,
               "Cin":self.cin

     }
