from nose.tools import *
from src.models import sonar

class TestCode:

    def test_sonar_should_exist(self): assert sonar

    def test_it_should_connect_to_the_database(self):
        connection = sonar.connect()
        assert connection

    def test_can_select_from_dual(self):
        connection = sonar.connect()
        rows = connection.query('select 1 from dual')
        assert len(rows) >= 1

    def test_select_all_sonars_from_route_1(self):
        rows = sonar.select_all_sonars_from('route_1_sonar')
        assert len(rows) >= 0
