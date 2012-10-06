from src.controllers import stop

from src.entry_point import *
from test.controllers.test_controller import *

class TestStopController(TestController):

    def test_can_show_stops(self):
        assert stop
        assert stop.index

    def test_can_show_specific_stops(self):
        assert stop.show

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_access_stops(self):
        self.request = self.testApp.get('/route/5/bus/8/stop')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('here are the routes associated with route 5')

    def test_access_specific_stop(self):
        self.request = self.testApp.get('/route/5/bus/8/stop/3')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('bus 8 for route 5 just landed at stop 3')



