import unittest
from models import source
Source = source.Source
class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source()