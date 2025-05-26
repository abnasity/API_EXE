from .extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    students = db.relationship("student", back_populates="Course")
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    course = db.Column(db.ForeignKey("course.id"))
    Course = db.relationship("course", back_populates="students")
    