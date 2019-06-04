'''
this Function calculates and returns the cost of each call, according to the rules:

If the call was shorter than 5 minutes, then you pay 3 cents
for every started second of the call
(e.g. for duration "00:01:07" you pay 67 * 3 = 201 cents).
If the call was at least 5 minutes long, then you pay 150 cents
for every started minute of the call
(e.g. for duration "00:05:00" you pay 5 * 150 = 750 cents
and for duration "00:05:01" you pay 6 * 150 = 900 cents).
'''

def getCost(duration):
    if duration > 5 * 60:    
         cost = (duration / 60)
         cost -= cost % -1
         cost *= 150
         cost = int(cost)        
    if duration <= 5 * 60:    
        cost = duration * 3
    return cost
