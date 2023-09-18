from random import choice as rc

from faker import Faker

from app import app
from models import db, Customer, ProductInventory, SalesOrder
# from models import customer_inventory_order

fake = Faker()


def create_customer():
    return Customer(name=fake.first_name()+' '+fake.last_name())


if __name__ == '__main__':
    with app.app_context():
        customers = [create_customer() for _ in range(5)]
        db.session.add_all(customers)
        db.session.commit()
