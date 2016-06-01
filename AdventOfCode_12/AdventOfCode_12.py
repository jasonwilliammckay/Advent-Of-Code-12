# Per http://adventofcode.com/day/12 parts one and two

import json

def parseDict(data):
    total = 0
    red = False

    for key, value in data.items():
        if type(value) is dict:
            total += parseDict(value)
        elif type(value) is list:
            total += parseList(value)
        elif type(value) is int:
            total += value
        elif type(value) is unicode and value == 'red':
            red = True

    return (0) if (red == True) else (total)

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
    total = parseDict(data)
    print ("The sum of everything, excluding 'red' objects, is {:,d}.".format(total))