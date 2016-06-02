import unittest

from AdventOfCode_12 import *

# Tests the Advent of Code 12 application
# Text is marked u"(string)" to reflect their unicode nature when imported from json by python

class Advent12_Test(unittest.TestCase):
    
    # The following are just the examples given by the question
    def test_parseDict_given(self):
        
        testObject =  dict({u"dummy":u"red",u"e":[1,2,3,4],u"f":5})
        self.assertEqual(parseDict(testObject), 0)

        testObject = dict({u"dummy":[1,{u"c":u"red",u"b":2},3]})
        self.assertEqual(parseDict(testObject), 4)

        testObject = dict({u"dummy":[1,2,3]})
        self.assertEqual(parseDict(testObject), 6)

        testObject = dict({u"dummy":[1,u"red",5]})
        self.assertEqual(parseDict(testObject), 6)

    # The following are variations of dictionaries that could be supplied
    def test_parseDict_comprehensive(self):
        # empty dict
        testObject = dict({})
        self.assertEqual(parseDict(testObject), 0)

        # simple dict
        testObject = dict({u"dummy":1})
        self.assertEqual(parseDict(testObject), 1)

        # simple dict with a negative number
        testObject = dict({u"dummy":-1})
        self.assertEqual(parseDict(testObject), -1)

        # simple dict with positive and negative numbers
        testObject = dict({u"dummy":1, u"dummy2":-3})
        self.assertEqual(parseDict(testObject), -2)

        # simple dict with a string, should be ignored
        testObject = dict({u"dummy":u"hello world"})
        self.assertEqual(parseDict(testObject), 0)

        # list nested in dict
        testObject =  dict({u"dummy":[1,2,3,4]})
        self.assertEqual(parseDict(testObject), 10)

        # dict nested in list
        testObject =  dict({u"dummy":[1,2,3,{u"b":2}]})
        self.assertEqual(parseDict(testObject), 8)

        # should ignore the presence of red in a list
        testObject =  dict({u"dummy":[1,2,3,u"red"]})
        self.assertEqual(parseDict(testObject), 6)

        # should sum the outer list, but omit the inner dict, owing to 'red' in both
        testObject =  dict({u"dummy":[1,2,u"red",3,{u"c":u"red",u"b":2}]})
        self.assertEqual(parseDict(testObject), 6)

        # should sum the outer list, but ignore the innermost list, because the dict calling it has 'red' as a value
        testObject =  dict({u"dummy":[1,2,3,{u"c":u"red",u"d":[99, 100, 101]}]})
        self.assertEqual(parseDict(testObject), 6)

        # should return zero since the outmost dict has red
        testObject =  dict({u"dummy":u"red", u"dummy2":[99, 100, [1, 2, 3]]})
        self.assertEqual(parseDict(testObject), 0)

if __name__ == '__main__':
    unittest.main()