from db import db


class BikeModel(db.Model):

    __tablename__ = 'bikes'

    bike_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    size = db.Column(db.String(200))
    price = db.Column(db.Float(precision=2))

    def __init__(self, _id, name, size, price):
        self.id = _id
        self.name = name
        self.size = size
        self.price = price

    def json(self):
        return {"name": self.name, "size": self.size, "price": self.price}

    @classmethod
    def get_all_bikes(cls):
        return cls.query.all()

    @classmethod
    def delete_all_rows(cls):
        db.session.query(BikeModel).delete()
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
