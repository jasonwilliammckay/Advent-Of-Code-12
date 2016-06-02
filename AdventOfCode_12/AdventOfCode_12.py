# Per http://adventofcode.com/day/12 parts one and two

import json

""" parseDict() accepts a unicode dictionary and iterates through it, keeping a running 
sum of integer values. Data can be nested several layers deep, so it uses recursion to 
solve this. To follow part 2 of a question, if 'red' is ever found as a value in a 
dictionary, the result of it and all children are automatically zero. There's no need 
to continue the operation. """

def parseDict(data):
    total = 0

    for key, value in data.items():
        if type(value) is dict:
            total += parseDict(value)
        elif type(value) is list:
            total += parseList(value)
        elif type(value) is int:
            total += value
        elif type(value) is unicode and value == 'red':
            return 0

    return total

""" parseList() accepts a list and iterates through it, keeping a running sum of
integer values. Unlike parseDict(), it does not care if a value is 'red' or not,
and will simply ignore it as a non-integer, though it will still process child
lists and dicts normally. """

def parseList(data):
    total = 0
    
    for i in data:
        if (type(i) is dict):
            total += parseDict(i)
        elif (type(i) is list):
            total += parseList(i)
        elif (type(i) is int):
            total += i

    return total

if __name__ == '__main__':
    data = json.loads(open('input.json','r').read())
    if (data is not None): total = parseDict(data)
    print ("The sum of everything, excluding 'red' objects, is {:,d}.".format(total))