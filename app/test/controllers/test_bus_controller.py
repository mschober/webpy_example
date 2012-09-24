from src.controllers import bus


class TestCode():

    def test_can_see_buses(self):
        assert bus
        assert bus.index

    def test_can_access_specific_bus(self):
        assert bus.show
