from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    options = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    consent = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Contact('{self.first_name}', '{self.last_name}', '{self.email}')"
