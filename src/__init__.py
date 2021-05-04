import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import routes

myapp = Flask(__name__)


db = SQLAlchemy(myapp)
mm = Marshmallow(myapp)
myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yalantis.db'
myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.create_all()
db.session.commit()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8090))
    myapp.run(host='0.0.0.0', port=port)
