from src import db
from datetime import datetime


class CourseModel(db.Model):

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String, nullable=False)
    course_lectures = db.Column(db.Integer, nullable=False)
    course_added_date = db.Column(db.String, nullable=False, default=datetime.now())
    course_start_date = db.Column(db.String, nullable=False)
    course_end_date = db.Column(db.String, nullable=False)

    def __init__(self, course_name=None,
                 course_description=None,
                 course_lectures=None,
                 course_added_date=None,
                 course_start_date=None,
                 course_end_date=None
                 ):
        self.course_name = course_name
        self.course_description = course_description
        self.course_lectures = course_lectures
        self.course_added_date = course_added_date
        self.course_start_date = course_start_date
        self.course_end_date = course_end_date


    @property
    def serialize(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_description': self.course_description,
            'course_lectures': self.course_lectures,
            'course_start_date': self.course_start_date,
            'course_added_date': self.course_added_date,
            'course_end_date': self.course_end_date
        }
