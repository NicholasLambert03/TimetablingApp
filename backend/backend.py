from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

filepath= os.path.join(os.path.dirname(__file__), 'connection_config.json')
with open(filepath) as config_file:
    config = json.load(config_file)

app.config.update(config)

mysql = MySQL(app)
# Route for seeing a data
@app.route('/data')
def content():
    # Returning an api for showing in  reactjs
    return {
        'field':'value'
    }
        
if __name__ == "__main__":
  app.run()