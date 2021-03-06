from paste.fixture import TestApp
from nose.tools import *
from src.code import app

class TestCode():
    def test_hello(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        request = testApp.get('/hello')
        assert_equal(request.status, 200)
        request.mustcontain('Hello, World!')
