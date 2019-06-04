'''
this function retuns the log.txt in String format
'''
def getLogAsString(file_name):

    f = open(file_name);
    #The given variable in the instructions S
    S = ""
    #read lines and concat to the string
    for line in f:
        S += line;

    return S;


