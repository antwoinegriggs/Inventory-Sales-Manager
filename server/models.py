from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)


class Inventory(db.Model, SerializerMixin):
    __tablename__ = 'Inventory'

    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String)
    product_number = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'<Inventory by {self.product}: {self.product_number}...>'
