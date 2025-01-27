from flask import jsonify
from app.services.student_service import find_students, add_student

def get_students():
    result = {
        "data": find_students()
    }
    return jsonify(result), 200

def create_student(data):
    result = {
        "data": add_student(data)
    }
    return jsonify(result), 201