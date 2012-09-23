from paste.fixture import TestApp
from nose.tools import *
import sys
from code import app

class TestCode():
    def test_hello(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/hello')
        assert_equal(r.status, 200)
        r.mustcontain('Hello, World!')
