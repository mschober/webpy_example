from nose.tools import *
from src.models import route

class TestCode:

    def test_it_should_connect_to_the_database(self):
        assert route
        assert route.connect()
