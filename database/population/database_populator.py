import sys
import os

original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'connection')))

from database_connector import Connector

sys.path = original_sys_path

cnx = Connector()
cnx.connect_to_database()

