import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

api = Flask(__name__)


db = SQLAlchemy(api)
mm = Marshmallow(api)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/yalantis_db.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from routes import *

db.create_all()
db.session.commit()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8090))
    api.run(host='0.0.0.0', port=port)
