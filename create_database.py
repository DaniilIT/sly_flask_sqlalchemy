from datetime import datetime
from init_app import app, db
from data.utils import upload_json
from models.user import User
from models.order import Order
from models.offer import Offer


def main():
    with app.app_context():
        db.drop_all()
        db.create_all()

        with db.session.begin():
            for user in upload_json('./data/users.json'):
                db.session.add(User(
                    id=user['id'],
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    age=user['age'],
                    email=user['email'],
                    role=user['role'],
                    phone=user['phone']
                ))

        with db.session.begin():
            for order in upload_json('./data/orders.json'):
                db.session.add(Order(
                    id=order['id'],
                    name=order['name'],
                    description=order['description'],
                    start_date=datetime.strptime(order['start_date'], '%m/%d/%Y'),
                    end_date=datetime.strptime(order['end_date'], '%m/%d/%Y'),
                    address=order['address'],
                    price=order['price'],
                    customer_id=order['customer_id'],
                    executor_id=order['executor_id']
                ))

        with db.session.begin():
            for offer in upload_json('./data/offers.json'):
                db.session.add(Offer(
                    id=offer['id'],
                    order_id=offer['order_id'],
                    executor_id=offer['executor_id']
                ))


if __name__ == '__main__':
    main()
