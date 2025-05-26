from .extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    
class Student(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(50), unique=True)
    course = db.Column(db.ForeignKey("course.id"))
    