from src.controllers import route
from test.controllers.test_controller import *


class TestRouteController(TestController):

    def test_route_displays_index(self):
        assert route
        assert route.index

    def test_shows_routes(self):
        assert route.show

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_url_mapping_to_route_controller(self):
        self.request = self.testApp.get('/route')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('Hey you found the route page!')

    def test_can_access_specific_route(self):
        self.request = self.testApp.get('/route/5')
        assert_equal(self.request.status, 200)
        self.request.mustcontain('the route you are seeing is 5')

