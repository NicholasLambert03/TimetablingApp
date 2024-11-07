import logging
import time
import mysql.connector

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler("cpy-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) 

def connect_to_database(config, attempts=3, delay=2):
    print("Beggining Connection")
    attempt = 1
    success = False
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            print("Connection Successful")
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger.info("Failed to connect, exiting without a connection: %s", err)
                return None
            logger.info(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts-1,
            )
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
    return None

config = {
  'user': 'root',
  'password': 'databaseaccess',
  'host': '127.0.0.1',
  'database':'university_timetable',
  'raise_on_warnings': True
}

def open_connection():
    connection = connect_to_database(config)
    cursor = connection.cursor()

def close_connection():
    cursor.close()
    connection.close()

