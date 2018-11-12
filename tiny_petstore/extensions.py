# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlathanor import FlaskBaseModel, initialize_flask_sqlathanor


db = SQLAlchemy(model_class=FlaskBaseModel)
db = initialize_flask_sqlathanor(db)


def _init_db(self, app=None):
    self.create_all(app=app)


db.init_db = type(db.init_app)(_init_db, db)
