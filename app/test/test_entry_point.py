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
        testApp = TestApp(app.wsgifunc(*middleware))
        self.request = testApp.get('/hello')

    def test_hello(self):
        assert_equal(self.request.status, 200)

    def test_hello_matches(self):
        self.request.mustcontain('Hello, World!')
