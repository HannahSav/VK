from flask import Blueprint, request, jsonify
from models import db, Product, Subcategory

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    product = Product(subcategory_id=data['subcategory_id'], name=data['name'], price=data['price'], image_url=data['image_url'], additional_fields=data['additional_fields'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'product_id': product.id}), 201
