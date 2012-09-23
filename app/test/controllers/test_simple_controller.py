from paste.fixture import TestApp
from nose.tools import *
from src.code import app

class TestCode():
    def test_hello_controller(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/hello/control')
        assert_equal(r.status, 200)
        r.mustcontain('Hello, World! I am in control')
