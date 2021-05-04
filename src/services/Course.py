from src.models import CourseModel


def get_all(filters):
    search = CourseModel.query.all()
    if not search:
        abort(404, message="Database is empty")


def get_one(id):
    return 'all courses'


def create_one_():
    return None


def update_one(id):
    return 'all courses'


def delete_one(id):
    return 'one deleted'

