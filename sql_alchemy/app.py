
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect+driver://root:triazine@123@host:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Import for Migrations

# Settings for migrations
# migrate = Migrate(app, db)