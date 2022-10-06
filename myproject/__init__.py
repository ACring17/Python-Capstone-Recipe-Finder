# Where the blueprints will be registered
from flask import Flask

app = Flask(__name__)

from myproject.core.views import core
from myproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
