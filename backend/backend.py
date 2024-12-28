from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import json
import logging

app = Flask(__name__)
CORS(app)

filepath= os.path.join(os.path.dirname(__file__), 'connection_config.json')
with open(filepath) as config_file:
    config = json.load(config_file)

app.config.update(config)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

mysql = MySQL(app)

conn = mysql.connect()
cursor = conn.cursor()

# Route for seeing a data
@app.route('/tables',methods=['GET'])
def content():
    app.logger.info('Processing request for /data')
    try:
        # Returning an api for showing in  reactjs
        cursor.execute('SHOW TABLES')
        tables = cursor.fetchall()
        return {
            
            'tables':'hi'
        }
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

        
if __name__ == "__main__":
  app.run(debug=True)