from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "tracker"}
app.config["SECRET_KEY"] = "KeepThisaS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from tracker.views import students
    ##from tracker.admin import admin
    app.register_blueprint(students)
    ##app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()

