from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class ProductInventory(db.Model, SerializerMixin):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20))
    product_number = db.Column(db.Integer)
    product_quantity = db.Column(db.Integer)
    product_price = db.Column(db.Integer)

    # Many-to-Many Customer
    inventory_customer = db.relationship(
        'Customer', secondary='customer_inventory_orders', overlaps='customer_inventory')

    # One-to-Many SalesOrder
    inventory_orders = db.relationship('SalesOrder')


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    # Many-to-Many ProductInventory
    customer_inventory = db.relationship(
        'ProductInventory', secondary='customer_inventory_orders', overlaps='customer_inventory')
    # One-to-Many SaleOrders
    customer_orders = db.relationship('SalesOrder')


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
        'Customer', secondary='customer_inventory_orders', overlaps='customer_inventory, inventory_customer')


# Join Table Customer, Inventory, Order
customer_inventory_order = db.Table(
    'customer_inventory_orders',
    db.Column("id", db.Integer, primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customers.id')),
    db.Column('product_inventory_id', db.Integer,
              db.ForeignKey('inventory.id')),
    db.Column('sales_order_id', db.Integer, db.ForeignKey('sales_orders.id'))
)
