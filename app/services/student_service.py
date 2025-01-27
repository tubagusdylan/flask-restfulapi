from app.models.student_model import Mahasiswa
import random

def find_students():
    return [student.to_dictionary() for student in Mahasiswa.query.all()]

def add_student(data):
    student = Mahasiswa(
        id=int(random.random() * 10),
        name=data["name"],
        npm=data["npm"],
        major=data["major"],
        faculty=data["faculty"],
        semester=data["semester"],
        year_in=data["year_in"]
    )
    student.save()
    return student.to_dictionary()