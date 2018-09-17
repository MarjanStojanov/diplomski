from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config())

db = SQLAlchemy(app)

migrate = Migrate(app, db)
ma = Marshmallow(app)


#for tbl in reversed(db.meta.sorted_tables):
#    db.engine.execute(tbl.delete())

import routes, api_routes , models
