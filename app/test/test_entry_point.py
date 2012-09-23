from paste.fixture import TestApp
from nose.tools import *
from src.entry_point import *

class TestCode():

    def test_app_wiring(self):
        assert urls >= 1
        assert render
        assert hello

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))
        self.request = self.testApp.get('/hello')

    def test_hello(self):
        assert_equal(self.request.status, 200)

    def test_hello_matches(self):
        self.request.mustcontain('Hello, World!')

    def test_url_mapping_to_route_controller(self):
        self.request = self.testApp.get('/route')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('Hey you found the route page!')

