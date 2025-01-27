from app import db

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    npm = db.Column(db.String(10), nullable=False)
    major = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(10), nullable=False)
    year_in = db.Column(db.Integer, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "npm": self.npm,
            "major": self.major,
            "faculty": self.faculty,
            "semester": self.semester,
            "year_in": self.year_in
        }