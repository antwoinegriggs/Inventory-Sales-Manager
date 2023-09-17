from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sku_number = db.Column(db.Integer)

    # One-to-Many ProductInventory
    inventory_items = db.relationship("ProductInventory")


class ProductInventory(db.Model, SerializerMixin):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)

    @property
    def product_name(self):
        return self.product.name
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    @property
    def product_number(self):
        return self.product.sku_number

    product_quantity = db.Column(db.Integer)
    product_price = db.Column(db.Integer)

    # Many-to-Many Customer
    inventory_customer = db.relationship(
        'Customer', secondary='customer_inventory_order', back_populates='customer_inventories')

    # One-to-Many SalesOrder
    inventory_orders = db.relationship('SalesOrder')


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    # (Many-to-Many) ProductInventory
    customer_inventory = db.relationship(
        'ProductInventory', secondary='customer_inventory_order', back_populates='customers_inventories')


class SalesOrder(db.Model):
    __tablename__ = 'sales_orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    order_number = db.Column(db.String(255))

    @property
    def customer_name(self):
        return self.product.name
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    @property
    def product_name(self):
        return self.product.product_name
    product_inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))

    quantity = db.Column(db.Integer)
    amount = db.Column(db.Float)

    # Many-to-Many Custoemr
    customer_order = db.relationship(
        'Customer', secondary='customer_inventory_order', back_populates='customer_orders')


# Join Table Customer, Inventory, Order
customer_inventory_order = db.Table(
    'customer_product_inventory',
    db.Column('customer_id', db.Integer, db.ForeignKey(
        'customers.id'), primary_key=True),
    db.Column('product_inventory_id', db.Integer,
              db.ForeignKey('inventory.id'), primary_key=True),
    db.Column('sales_order_id', db.Integer, db.ForeignKey(
        'sales_orders.id'), primary_key=True)
)
