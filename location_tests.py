import unittest
from location import *

class TestLab1(unittest.TestCase):
    
    #testing __init__ method
    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)
    
    #testing __eq__ method
    def test_eq(self):
        loc1 = Location("Test Place", 12.3, -456.7)
        loc2 = Location("Test Place", 12.3, -456.7)
        self.assertEqual((loc1==loc2), True)
    
    #testing __repr__ method
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

if __name__ == "__main__":
        unittest.main()
