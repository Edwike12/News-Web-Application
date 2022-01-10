from flask import Flask
from config import config_options


# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(config_options[config_name])


from app import views