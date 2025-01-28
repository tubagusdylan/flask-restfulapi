from app.models.student_model import Mahasiswa
import random

def find_students():
    return [student.to_dictionary() for student in Mahasiswa.query.all()]

def find_student(id):
    student = Mahasiswa.query.get(id)
    if not student:
        return "Student not found"
    
    return student.to_dictionary()

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

def update(data, id):
    student = Mahasiswa.query.get(id)
    if not student:
        return "Student not found"

    student.name = data["name"]
    student.npm = data["npm"]
    student.major = data["major"]
    student.faculty = data["faculty"]
    student.semester = data["semester"]
    student.year_in = data["year_in"]

    student.commit()
    return student.to_dictionary()

def delete(id):
    student = Mahasiswa.query.get(id)
    if not student:
        return "Student not found"
    
    student.delete()
    return "Delete success"