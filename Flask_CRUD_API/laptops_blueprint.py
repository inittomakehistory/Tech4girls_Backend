from flask import Blueprint, request, jsonify
from yourapplication.models import Laptop
from yourapplication import db

laptops_blueprint = Blueprint('laptops', __name__)

@laptops_blueprint.route('/laptops/add', methods=['POST'])
def add_laptop():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    name = data.get('name')
    laptop_number = data.get('laptop_number')
    specifications = data.get('specifications')

    if not all([name, laptop_number, specifications]):
        return jsonify({'message': 'Missing required fields'}), 400

    existing_laptop = Laptop.query.filter_by(laptop_number=laptop_number).first()
    if existing_laptop:
        return jsonify({'message': 'Laptop number already exists'}), 400

    new_laptop = Laptop(name=name, laptop_number=laptop_number, specifications=specifications)
    db.session.add(new_laptop)
    db.session.commit()

    return jsonify({'message': 'Laptop added successfully'}), 201
