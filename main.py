'''


The logs are given as a string S consisting of N lines separated by end-of-line characters
 Each line describes one phone call using the following format: “hh:mm:ss,nnn-nnn-nnn”, where
“hh:mm:ss” denotes the duration of the call (in “hh” hours, “mm” minutes and “ss” seconds) and
“nnn-nnn-nnn” denotes the 9-digit phone number of the recipient (with no leading zeros).

Each call is billed separately. The billing rules are as follows:

    
among these phone numbers.


Write a function solution that, given a string S describing phone call logs, returns the amount of
money you have to pay in cents.
For example, given string S with N = 3 lines:
“00:01:07,400-234-090
00:05:01,701-080-080
00:05:00,400-234-090”

The function should return 900 (the total duration for number 400-234-090 is 6 minutes 7 seconds,
and the total duration for number 701-080-080 is 5 minutes 1 second; therefore, the free promotion
applies to the former phone number).
Assume that:
• N is an integer within the range [1..100];
• Every phone number follows the format “nnn-nnn-nnn” strictly; there are no leading zeros;
• The duration of every call follows the format “hh:mm:ss” strictly;
• Each line follows the format “hh:mm:ss,nnn-nnn-nnn” strictly; there are no empty lines and
spaces.

'''

from getFinalNumInfoArray import getFinalNumInfoArray
from getLogAsString import getLogAsString
from findFreeNumber import findFreeNumber
from getFreeCalls import getFreeCalls
from getSelectedInfo import getSelectedInfo

# First, we read del calls file
file_name = 'logs.txt'#put here name of the logs file

strFile = getLogAsString(file_name)



def getCallsInfo():
    
    finalNumInfoArray = getFinalNumInfoArray(strFile);
    free_number = findFreeNumber(finalNumInfoArray);
    target = getSelectedInfo(strFile);
    info = getFreeCalls(free_number, target);

    for i in info:
        print(i);
    

        

if __name__ == '__main__':
    
    getCallsInfo();
    print('PROGRAM FINISHED');
    a = input('press Enter to exit');



