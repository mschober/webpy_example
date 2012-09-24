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
        assert_equal(0, len(rows))

    def test_insert_rows_into_route_1_sonar(self):
        inserted = sonar.bus_landed('route_1_sonar', 1, 1)
        rows = sonar.select_all_sonars_from('route_1_sonar')
        assert len(rows) == 1 
        sonar.connect().delete('route_1_sonar', where='1=1')
