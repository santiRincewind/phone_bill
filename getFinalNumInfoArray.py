from getAllNumInfoArray import getAllNumInfoArray
from getSetNumbers import getSetNumbers
from getArrayUniqueMembers import getArrayUniqueMembers
from getInfoNumSum import getInfoNumSum
'''
This function returns all information about calls and shows the total cost
and duration(in seconds) for each number dialed.
'''
def getFinalNumInfoArray(strFile):
    numAllInfoArray = getAllNumInfoArray(strFile);
    numbersSet = getSetNumbers(numAllInfoArray);
    arrayUniqueMembers = getArrayUniqueMembers(numbersSet);
    finalNumSumInfo = getInfoNumSum(arrayUniqueMembers, numAllInfoArray);
    return finalNumSumInfo;


