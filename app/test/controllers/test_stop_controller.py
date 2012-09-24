from src.controllers import stop

class TestCode():

    def test_can_show_stops(self):
        assert stop
        assert stop.index

    def test_can_show_specific_stops(self):
        assert stop.show
