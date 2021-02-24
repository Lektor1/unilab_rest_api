from db import db


class UserModel(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def json(self):
        return {}

    @classmethod
    def find_by_username(cls, username):
        user_data = cls.query.filter_by(username=username).first()

        if user_data:
            return cls(user_data.user_id, user_data.username, user_data.password)
        else:
            return None

    @classmethod
    def find_by_userid(cls, user_id):
        user_data = vars(cls.query.filter_by(user_id=user_id).first())

        if user_data:
            return cls(user_data['user_id'], user_data['username'], user_data['password'])
        else:
            return None

    def add(self):
        db.session.add(self)
        db.session.commit()