from nose.tools import *
from src.models import route

class TestCode:

    def test_route_should_exist(self): assert route

    def test_it_should_connect_to_the_database(self):
        connection = route.connect()
        assert connection

    def test_can_select_from_dual(self):
        connection = route.connect()
        rows = connection.query('select 1 from dual')
        assert len(rows) >= 1
