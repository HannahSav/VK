from flask import Blueprint, request, jsonify
from models import db, Warehouse

bp = Blueprint('warehouses', __name__, url_prefix='/warehouses')

@bp.route('/', methods=['GET'])
def get_warehouses():
    warehouses = Warehouse.query.all()
    return jsonify([warehouse.to_dict() for warehouse in warehouses])

@bp.route('/', methods=['POST'])
def create_warehouse():
    data = request.json
    warehouse = Warehouse(city_id=data['city_id'], name=data['name'], address=data['address'])
    db.session.add(warehouse)
    db.session.commit()
    return jsonify({'warehouse_id': warehouse.id}), 201
