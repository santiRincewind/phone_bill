'''
Returns the dictionary of unique numbers(numbers_set)
with 0 value of cost and duration of calls for each number.
'''

def getArrayUniqueMembers(numbersSet):
    arrayUniqueMembers = [];    
    for i in numbersSet:        
        data = {'number': i, 'cost' : 0, 'duration':  0 };
        arrayUniqueMembers.append(data);
    return arrayUniqueMembers;
