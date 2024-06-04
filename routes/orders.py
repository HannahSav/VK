from flask import Blueprint, request, jsonify
from models import db, Order, OrderItem

bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('/', methods=['POST'])
def create_order():
    data = request.json
    order = Order(user_id=data['user_id'], total_price=data['total_price'], status='pending')
    db.session.add(order)
    db.session.commit()

    for item in data['items']:
        order_item = OrderItem(order_id=order.id, product_id=item['product_id'], quantity=item['quantity'],
                               price=item['price'])
        db.session.add(order_item)

    db.session.commit()
    return jsonify({'order_id': order.id}), 201
