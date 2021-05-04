from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from src.services.Course import *

from src import myapp


@myapp.route('/courses', methods=['GET'])
def get_all_courses():
    return jsonify(get_all(None))


@myapp.route('/course/<id>', methods=['GET', 'PATCH', 'DELETE'])
def one_course(course_id):
    course_id = id
    if request.method == 'DELETE':
        return jsonify(delete_one(course_id))
    if request.method == 'PATCH':
        return jsonify(update_one(course_id))
    if request.method == 'GET':
        return jsonify(get_one(course_id))


@myapp.route('/course>', methods=['POST'])
def create_course():
    return jsonify(create_one_());