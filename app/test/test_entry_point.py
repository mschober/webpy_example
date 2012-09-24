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

    def test_can_access_specific_route(self):
        self.request = self.testApp.get('/route/5')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('the route you are seeing is 5')

    def test_can_access_bus_page_from_routes(self):
        self.request = self.testApp.get('/route/5/bus')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('here are the buses associated with 5')

    def test_can_access_a_specific_bus(self):
        self.request = self.testApp.get('/route/5/bus/8')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('what do you want to do with bus 8?')

    def test_access_stops(self):
        self.request = self.testApp.get('/route/5/bus/8/stop')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('here are the routes associated with route 5')

    def test_access_specific_stop(self):
        self.request = self.testApp.get('/route/5/bus/8/stop/3')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('bus 8 for route 5 just landed at stop 3')



