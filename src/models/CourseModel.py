from src import db
from datetime import datetime


class CoursesModel(db.Model):

    Course_id = db.Column(db.Integer, primary_key=True)
    Course_name = db.Column(db.String, nullable=False)
    Course_description = db.Column(db.String, nullable=False)
    Course_lectures = db.Column(db.Integer, nullable=False)
    Course_added_date = db.Column(db.Date, nullable=False, default=datetime.now())
    Course_start_date = db.Column(db.Date, nullable=False)
    Course_end_date = db.Column(db.Date, nullable=False)

db.create_all()