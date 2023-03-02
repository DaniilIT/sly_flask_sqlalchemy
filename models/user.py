from init_app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(40))
    role = db.Column(db.String(20), default='customer')
    phone = db.Column(db.String(20))


    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role,
            'phone': self.phone,
        }
