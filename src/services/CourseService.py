from src.models.CourseModel import CourseModel
from src.schemas.Course import CourseSchema
from flask import abort
from src import db
from flask import request


def get_all(args=None):


    if args:

        if 'course_name' in args:
                return CourseSchema(many=True).dump(
                    CourseModel.query.filter(CourseModel.course_name.contains(args['course_name'])))

        if 'start_date' in args:
                return CourseSchema(many=True).dump(CourseModel.query.filter_by(course_start_date=args['start_date']))

        if 'end_date' in args:
                return CourseSchema(many=True).dump(CourseModel.query.filter_by(course_end_date=args['end_date']))

        if 'lectures' in args:
                return CourseSchema(many=True).dump(CourseModel.query.filter_by(course_lectures=args['lectures']))



    return CourseSchema(many=True).dump(CourseModel.query.all())


def get_one(course_id):
    return CourseModel.query.filter_by(course_id=course_id).first().serialize


def create_one_(data):
    course = CourseModel.query.filter_by(course_name=data['course_name']).first()
    if course:
        abort(409, 'Course already exists')

    New = CourseModel(course_name=data['course_name'],
                      course_description=data['course_description'],
                      course_start_date=data['course_start_date'],
                      course_end_date=data['course_end_date'],
                      course_lectures=data['course_lectures'])

    db.session.add(New)
    db.session.commit()
    return New.serialize


def update_one(course_id, data):
    course = CourseModel.query.filter_by(course_id=course_id).first()
    if not course:
        abort(409, "Course doesn't exist,cannot update")

    if data['course_name']:
        course.course_name = data['course_name']
    if data['course_description']:
        course.course_description = data['course_description']
    if data['course_lectures']:
        course.course_lectures = data['course_lectures']
    if data['course_start_date']:
        course.course_start_date = data['course_start_date']
    if data['course_end_date']:
        course.course_end_date = data['course_end_date']
    course.course_id = course_id

    db.session.commit()
    return course.serialize


def delete_one(course_id):
    course = CourseModel.query.filter_by(course_id=course_id).first()
    if not course:
        abort(404, "Course with that ID doesn't exist, cannot delete")

    db.session.delete(course)
    db.session.commit()

    return 204, course.serialize
