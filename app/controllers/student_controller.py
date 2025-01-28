from flask import jsonify
from app.services.student_service import find_students, find_student, add_student, update, delete

def get_students():
    result = {
        "data": find_students()
    }
    return jsonify(result), 200

def get_student(id):
    result = {
        "data": find_student(id)
    }
    return jsonify(result), 200

def create_student(data):
    result = {
        "data": add_student(data)
    }
    return jsonify(result), 201

def update_student(data, id):
    result = {
        "data": update(data, id)
    }
    return jsonify(result), 201

def delete_student(id):
    result = {
        "data": delete(id)
    }
    return jsonify(result), 200