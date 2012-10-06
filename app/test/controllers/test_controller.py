from nose.tools import *
from paste.fixture import TestApp
from src.entry_point import app

class TestController():

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))
