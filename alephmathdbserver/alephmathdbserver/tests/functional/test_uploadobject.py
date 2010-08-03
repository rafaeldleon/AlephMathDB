from alephmathdbserver.tests import *

class TestUploadobjectController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='uploadobject', action='index'))
        # Test response...
