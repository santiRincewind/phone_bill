'''
This function accepts array of dictionaries(ArrayNumAllInfo),
each dictionary contains: number, cost and duration of the call.

Returns the set of call numbers - numbersSet.
'''

def getSetNumbers(ArrayNumAllInfo):
    numbersSet = set();
    for i in ArrayNumAllInfo:
        numbersSet.add(i['number']);
        
    return numbersSet;
