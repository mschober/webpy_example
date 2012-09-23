from paste.fixture import TestApp
from nose.tools import *
from src.entry_point import *

class TestCode():


    def test_app_wiring(self):
        assert urls >= 1
        assert render
        assert hello

    def test_hello(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        request = testApp.get('/hello')
        assert_equal(request.status, 200)

