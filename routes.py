from flask import jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from src.services.CourseService import *

from src import api


@api.route('/ping', methods=['GET'])
def pong():
    return jsonify('pong')


@api.route('/courses', methods=['GET'])
def get_all_courses():
    course_name = request.args.get('name')
    course_start_date = request.args.get('date')
    return jsonify(get_all(course_name, course_start_date))


@api.route('/course/<id>', methods=['GET', 'PATCH', 'DELETE'])
def one_course(id):
    course_id = id
    if request.method == 'DELETE':
        return jsonify(delete_one(course_id))
    if request.method == 'PATCH':
        return jsonify(update_one(course_id))
    if request.method == 'GET':
        return jsonify(get_one(course_id))


@api.route('/course', methods=['POST'])
def create_course():
    return jsonify(create_one_(request.json))