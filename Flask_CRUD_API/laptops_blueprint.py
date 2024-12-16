from flask import Blueprint, request, jsonify
from laptop_crud import Laptop_crud
from config import session  

# Create the Blueprint
laptops_blueprint = Blueprint('laptops', __name__)

# Initialize the CRUD class to handle laptop operations
laptop_crud = Laptop_crud(session)

# Add a Laptop
@laptops_blueprint.route('/add', methods=['POST'])
def add_laptop():
    data = request.get_json()
    
    
    if not data or not all(field in data for field in ['laptop_name', 'laptop_number', 'student_id']):
        return jsonify({"error": "Missing required fields: laptop_name, laptop_number, student_id"}), 400

    laptop_name = data['laptop_name']
    laptop_number = data['laptop_number']
    student_id = data['student_id']
    
    # Check if laptop number already exists
    if laptop_crud.get_laptop_by_id(laptop_number):
        return jsonify({"error": "Laptop number already exists"}), 400
    
    # Insert new laptop
    new_laptop = laptop_crud.insert_laptop(laptop_name, laptop_number, student_id)
    
    # Returns laptop
    return jsonify({
        "message": "Laptop added successfully",
        "laptop": {
            "laptop_name": new_laptop.laptop_name,
            "laptop_number": new_laptop.laptop_number,
            "student_id": new_laptop.student_id
        }
    }), 201

# Get_All _Laptops
@laptops_blueprint.route('', methods=['GET'])
def get_all_laptops():
    laptops = laptop_crud.get_all_laptops()
    return jsonify([{
        "laptop_name": laptop.laptop_name,
        "laptop_number": laptop.laptop_number,
        "student_id": laptop.student_id
    } for laptop in laptops]), 200


# Get_Laptop_by_Name
@laptops_blueprint.route('/name/<string:laptop_name>', methods=['GET'])
def get_laptop_by_name(laptop_name):
    laptop = laptop_crud.get_laptop_by_name(laptop_name)
    if not laptop:
        return jsonify({"error": "Laptop not found"}), 404
    return jsonify({
        "laptop_name": laptop.laptop_name,
        "laptop_number": laptop.laptop_number,
        "student_id": laptop.student_id
    }), 200


# Get_Laptop_by_Laptop_Number
@laptops_blueprint.route('/number/<int:laptop_number>', methods=['GET'])
def get_laptop_by_number(laptop_number):
    laptop = laptop_crud.get_laptop_by_id(laptop_number)
    if not laptop:
        return jsonify({"error": "Laptop not found"}), 404
    return jsonify({
        "laptop_name": laptop.laptop_name,
        "laptop_number": laptop.laptop_number,
        "student_id": laptop.student_id
    }), 200


# Update_Laptop_by_Laptop_Number
@laptops_blueprint.route('/update/<int:laptop_number>', methods=['PUT'])
def update_laptop(laptop_number):
    data = request.get_json()

    # Check_if_laptop_exists
    laptop = laptop_crud.get_laptop_by_id(laptop_number)
    if not laptop:
        return jsonify({"error": "Laptop not found"}), 404

    laptop_name = data.get('laptop_name', laptop.laptop_name)
    student_id = data.get('student_id', laptop.student_id)

    # Update_laptop_details
    updated_laptop = laptop_crud.update_laptop(laptop_number, laptop_name, student_id)
    
    return jsonify({
        "message": "Laptop updated successfully",
        "laptop": {
            "laptop_name": updated_laptop.laptop_name,
            "laptop_number": updated_laptop.laptop_number,
            "student_id": updated_laptop.student_id
        }
    }), 200

# Delete_Laptop_by_Laptop_Number
@laptops_blueprint.route('/delete/<int:laptop_number>', methods=['DELETE'])
def delete_laptop(laptop_number):
    laptop = laptop_crud.get_laptop_by_id(laptop_number)
    if not laptop:
        return jsonify({"error": "Laptop not found"}), 404

    # Delete_the_laptop
    message = laptop_crud.delete_laptop(laptop_number)
    return jsonify({"message": message}), 200
