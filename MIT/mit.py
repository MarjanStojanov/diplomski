from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config())

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__=='__main__':
	app.run(port=5001)
import routes , models
