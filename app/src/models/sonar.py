from config import db

def connect():
    return db

def select_all_sonars_from(route):
    return connect().query('select * from ' + route)
