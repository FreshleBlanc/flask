from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = dbColumn(db.String(50), unique= True)
    username = db.Column(dbString)