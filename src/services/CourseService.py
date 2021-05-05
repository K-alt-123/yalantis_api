from src.models.CourseModel import CourseModel
from src.schemas.Course import CourseSchema
from flask import abort
from src import db


def get_all(name=None,date=None):
    data = CourseModel.query.all()
    return CourseSchema(many=True).dump(data)


def get_one(course_id):
    return CourseModel.query.filter_by(course_id=course_id).first().serialize


def create_one_(data):
    course = CourseModel.query.filter_by(course_name=data['course_name']).first()
    if course:
        abort(409, message='Course already exists')
    db.session.add(data)
    db.session.commit()
    return data


def update_one(id):
    return 'all courses'


def delete_one(id):
    return 'one deleted'

