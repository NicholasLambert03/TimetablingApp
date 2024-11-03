import sys
import os
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'connection')))
from database_connector import Connector
sys.path = original_sys_path



class Populator():
    def __init__(self):
        self.cnx = Connector()
        self.cnx.connect_to_database()
    def add_course(self,course_id,course_name):
        '''Add a new course to the database
        Params:
        course_id (string): unique id of course
        course_name (string): name of course'''
        self.cnx.cursor.execute()

populator = Populator()