import logging
import time
import mysql.connector
import json
import os

class Connector:
    def __init__(self):
        
        # Set up logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Log to console
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

        # Also log to a file
        self.file_handler = logging.FileHandler("database\connection\connector-errors.log")
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        #Set up config filepath
        self.config_file_path = 'database\connection\connection_config.txt'
    def connect_to_database(self):
        def establish_connection(self,attempts=3, delay=2):
            print("Beggining Connection")
            attempt = 1
            # Implement a reconnection routine5
            while attempt < attempts + 1:
                try:
                    self.connection = mysql.connector.connect(**self.get_config())
                    self.cursor = self.connection.cursor()
                    return True
                except (mysql.connector.Error, IOError) as err:
                    if (attempts is attempt):
                        # Attempts to reconnect failed; returning None
                        self.logger.info("Failed to connect, exiting without a connection: %s", err)
                        return None
                    self.logger.info(
                        "Connection failed: %s. Retrying (%d/%d)...",
                        err,
                        attempt,
                        attempts-1,
                    )
                    # progressive reconnect delay
                    time.sleep(delay ** attempt)
                    attempt += 1
            return False
        if establish_connection(self,):
            print("Connected")
        else:
            print('Connection Failed')  
    def disconnect_from_database(self,):
        self.cursor.close
        self.connection.close()
    def get_config(self,):
        print("Getting config")
        with open(self.config_file_path) as f:
            data = f.read()
        config = json.loads(data)
        print(f'Config: {config}')
        return config