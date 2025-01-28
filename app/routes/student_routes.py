from flask import Blueprint, request
from app.controllers.student_controller import get_students, get_student, create_student, update_student, delete_student

student_bp = Blueprint("student_blueprint", __name__)

@student_bp.route("/<int:id>", methods=["GET"])
def student(id):
    return get_student(id)

@student_bp.route("/<int:id>", methods=["PUT"])
def edit_student(id):
    return update_student(request.json, id)

@student_bp.route("/<int:id>", methods=["DELETE"])
def del_student(id):
    return delete_student(id)

@student_bp.route("/", methods=["POST"])
def add_student():
    return create_student(request.json)

@student_bp.route("/", methods=["GET"])
def students():
    return get_students()
