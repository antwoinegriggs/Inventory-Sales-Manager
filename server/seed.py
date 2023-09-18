from random import choice
from random import randint

from faker import Faker

from app import app
from models import db, Customer, ProductInventory, SalesOrder
# from models import customer_inventory_order

fake = Faker()


def create_customer():
    return Customer(name=fake.first_name()+' '+fake.last_name())


def create_inventory():
    return ProductInventory(
        product_name=fake.word(),
        product_number=randint(1000, 9999),
        product_quantity=randint(1, 100),
        product_price=randint(1, 100)
    )


if __name__ == '__main__':
    with app.app_context():
        # customer
        customers = [create_customer() for _ in range(5)]
        db.session.add_all(customers)

        # inventory
        products = [create_inventory() for _ in range(10)]
        db.session.add_all(products)

        db.session.commit()
