from flask import Flask
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

with open('backend\connection_config.json') as config_file:
    config = json.load(config_file)

app.config.update(config)

mysql = MySQL(app)
# Route for seeing a data
@app.route('/')
def content():

    # Returning an api for showing in  reactjs
    return 'web'
        
if __name__ == "__main__":
  app.run()