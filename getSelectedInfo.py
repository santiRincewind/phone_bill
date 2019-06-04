from getAllNumInfoArray import getAllNumInfoArray;
from getFinalNumInfoArray import getFinalNumInfoArray;
'''
This function retrieves the info about call or numbers according to the user selection
if option calls is seected, the function rerurn an array containg the cost and duration of all the calls 
stored in the log.txt file

if option numbers is selected, the function returns an array containing info of the numbers stored in the 
logs.txt file, adding the duration and the cost of all the calls
'''
def getSelectedInfo(strFile):
    print('Hello');
    print('This program shows info about the phone calls stored in the file calls.txt');
    print('first, decide how the information will be shown');
    print ('type "calls" to show the info of each indididual call');
    print('type "numbers" to show the info of each indidual number ');
    print('Please make your choice:');
    print('for calls enter "calls", for numbers enter "numbers"');
    
    #request input param
    c = input('write your choice here: ');
    
    if c == 'calls':
        numAllInfoArray = getAllNumInfoArray(strFile);
        return numAllInfoArray;
        
    if c == 'numbers':
        finalNumInfoArray = getFinalNumInfoArray(strFile);
        return finalNumInfoArray;

    

