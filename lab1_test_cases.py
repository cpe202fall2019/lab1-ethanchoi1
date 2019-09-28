#things to consider
#non-integer input, multiple targets?, duplicate values
#target is not in the bin_search list

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    #tests for ValueError raised when None is passed
    def test_max_list_iter_00(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
            
    #basic largest value test
    def test_max_list_iter_01(self):
        self.assertEqual(max_list_iter([0,2,3,6,4,1,5]),6)
    
    #basic largest value test
    def test_max_list_iter_02(self):
        self.assertEqual(max_list_iter([-9,-5,-3,8,0,2,-4,6]),8)

    #test when there are duplicate values
    def test_max_list_iter_03(self):
        self.assertEqual(max_list_iter([-1,0,5,9,9,10,7,7]),10)
        
    #test when list is empty
    def test_max_list_iter_04(self):
        self.assertEqual(max_list_iter([]),None)
#--------------------------------------------------------------------------
    #basic list reversal test
    def test_reverse_rec_00(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    #basic list reversal test
    def test_reverse_rec_01(self):
        self.assertEqual(reverse_rec([1,10,2,2,4]),[4,2,2,10,1])
    
    #tests for ValueError raised when None is passed
    def test_reverse_rec_03(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
            
    #tests for empty list input
    def test_reverse_rec_01(self):
        self.assertEqual(reverse_rec([]),[])
    
#--------------------------------------------------------------------------
    #basic binary search test
    def test_bin_search_00(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
    
    #basic binary search test with negative numbers
    #target in left middle value
    def test_bin_search_01(self):
       list_val =[-10,-7,-6,-4,-2,-1,0,3,5,8,9,10]
       low = 0
       high = len(list_val)-1
       self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 6)
    
    #target in right middle value
    def test_bin_search_02(self):
        list_val =[-10,-7,-6,-4,-2,-1,0,3,5,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), 5)
    
    #3 length array
    def test_bin_search_03(self):
        list_val = [0,1,2]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2,0,len(list_val)-1,list_val), 2)
    
    #target is not in array
    def test_bin_search_04(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None)
        
    #list is None
    def test_bin_search_05(self):
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0,0,0,tlist)
    
    #2 length array
    def test_bin_search_06(self):
        list_val = [2,3]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 1)

    #1 length array
    def test_bin_search_07(self):
        list_val = [9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 0)
        
    #0 length array
    def test_bin_search_08(self):
        list_val = []
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), None)
        
    #target in first value of list
    def test_bin_search_09(self):
        list_val =[-10,-7,-6,-4,-2,-1,0,3,5,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-10, 0, len(list_val)-1, list_val), 0)
        
    #target in last value of list
    def test_bin_search_10(self):
        list_val =[-10,-7,-6,-4,-2,-1,0,3,5,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 11)
    

if __name__ == "__main__":
        unittest.main()