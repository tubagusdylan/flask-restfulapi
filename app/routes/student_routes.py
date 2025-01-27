from flask import Blueprint, request
from app.controllers.student_controller import get_students, create_student

student_bp = Blueprint("student_blueprint", __name__)

@student_bp.route("/", methods=["GET"])
def students():
    return get_students()

@student_bp.route("/", methods=["POST"])
def add_student():
    return create_student(request.json)