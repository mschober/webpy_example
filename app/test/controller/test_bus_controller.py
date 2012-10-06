from src.controller import bus
from test.controller.test_controller import *


class TestBusController(TestController):

    def test_can_see_buses(self):
        assert bus
        assert bus.index

    def test_can_access_specific_bus(self):
        assert bus.show

    def test_can_access_bus_page_from_routes(self):
        self.request = self.testApp.get('/route/5/bus')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('here are the buses associated with 5')

    def test_can_access_a_specific_bus(self):
        self.request = self.testApp.get('/route/5/bus/8')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('what do you want to do with bus 8?')

