from flask import Flask, request, jsonify
from flask_sqlachemy import SQLAlchemy
from flask_marshmellow import Marshmellow
import os

# Initialises the application
app = Flask(__name__)

# Initialises the server
if __name__ == '__main__':
    app.run(debug=True)