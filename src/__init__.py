from flask import Flask
from config import Config
from flask_cors import CORS
from .database.personas import reset_table

from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

CORS(app)

app.register_blueprint(global_scope, url_prefix='/')
app.register_blueprint(errors_scope, url_prefix='/')
app.register_blueprint(api_scope, url_prefix='/api')