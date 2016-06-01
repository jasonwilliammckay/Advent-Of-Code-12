import unittest

from AdventOfCode_12 import *

# Tests the Advent of Code 12 application
# Text is marked u"(string)" to reflect their unicode nature when imported from json by python

class Advent12_Test(unittest.TestCase):
    
    def test_parseDict(self):
        
        testObject =  dict({u"dummy":u"red",u"e":[1,2,3,4],u"f":5})
        self.assertEqual(parseDict(testObject), 0)

        testObject = dict({u"dummy":[1,{u"c":u"red",u"b":2},3]})
        self.assertEqual(parseDict(testObject), 4)

        testObject = dict({u"dummy":[1,2,3]})
        self.assertEqual(parseDict(testObject), 6)

        testObject = dict({u"dummy":[1,u"red",5]})
        self.assertEqual(parseDict(testObject), 6)

if __name__ == '__main__':
    unittest.main()