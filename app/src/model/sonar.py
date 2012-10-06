from web import SQLLiteral
from config import db

def connect():
    return db

def select_all_sonars_from(route):
    return connect().query('select * from ' + route)

def bus_landed(route, bus, stop):
    return connect().insert(route, bus_id=bus, stop_id=stop, stopped_at=SQLLiteral('NOW()'))

