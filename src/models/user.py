from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.firstname,
            "lastName": self.lastname,
            "age": self.age,
        }
