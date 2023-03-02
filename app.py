from datetime import datetime
from flask import request, jsonify, abort, redirect
from init_app import app, db
from models.user import User
from models.order import Order
from models.offer import Offer


@app.route('/users/', methods=['GET', 'POST'])
def users_page():
    if request.method == 'GET':
        return jsonify([user.to_dict() for user in User.query.all()])
    else:
        user = request.json
        with db.session.begin():
            db.session.add(User(**user))
        return redirect(f'/users/{user["id"]}', 303)



@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_page(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(user.to_dict())

    elif request.method == 'PUT':
        user_data = request.json

        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        with db.session.begin():
            db.session.add(user)

        return redirect(f'/users/{user_id}', 303)

    else:
        db.session.delete(user)
        db.session.commit()
        return redirect('/users/', 303)


@app.route('/orders/', methods=['GET', 'POST'])
def orders_page():
    if request.method == 'GET':
        return jsonify([order.to_dict() for order in Order.query.all()])
    else:
        order = request.json
        with db.session.begin():
            db.session.add(Order(**order))
        return redirect(f'/orders/{order["id"]}', 303)


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order_page(order_id):
    order = Order.query.get(order_id)
    if order is None:
        abort(404)

    if request.method == 'GET':
        customer = order.customer.first_name
        executor = order.executor.first_name
        return jsonify(order.to_dict(customer, executor))

    elif request.method == 'PUT':
        order_data = request.json

        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = datetime.strptime(order['start_date'], '%m/%d/%Y')
        order.end_date = datetime.strptime(order['end_date'], '%m/%d/%Y')
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']

        with db.session.begin():
            db.session.add(order)

        return redirect(f'/order/{order_id}', 303)

    else:
        db.session.delete(order)
        db.session.commit()
        return redirect('/orders/', 303)




@app.route('/offers/', methods=['GET', 'POST'])
def offers_page():
    if request.method == 'GET':
        return jsonify([offer.to_dict() for offer in Offer.query.all()])
    else:
        offer = request.json
        with db.session.begin():
            db.session.add(Offer(**offer))
        return redirect(f'/offers/{offer["id"]}', 303)


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def offer_page(offer_id):
    offer = Offer.query.get(offer_id)
    if offer is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(offer.to_dict())

    elif request.method == 'PUT':
        offer_data = request.json

        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        with db.session.begin():
            db.session.add(offer)

        return redirect(f'/offer/{offer_id}', 303)

    else:
        db.session.delete(offer)
        db.session.commit()
        return redirect('/offers/', 303)


if __name__ == '__main__':
    # db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
