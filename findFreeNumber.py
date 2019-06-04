'''
All calls to the phone number that has the longest total duration of calls
are free. In the case of a tie, if more than one phone number shares the
longest total duration, the promotion is applied only to the phone number
whose numerical value is the smallest among these phone numbers.

returns number with free cost of all calls 
'''

def get_max_duration(arr):
    
    arr.sort()
    arr.reverse()
    
    return arr[0]


def findFreeNumber(final_num_info_dicts_array):
    
    data_1 = []#contains all values of duration 

    for i in final_num_info_dicts_array:
        data_1.append(i['duration'])


    #contains max value of duration 
    data_2 = get_max_duration(data_1)

    #contains dict(s), whis number(s) with max duration
    data_3 = []

    for i in final_num_info_dicts_array:
        
        if data_2 == i['duration']:
            data_3.append(i)
 

    l = 0
    for i in data_3:
        l += 1

    #array with dict(s), which contains number and number numerical value
    data_4 = []
    
    if l > 1:
        ''' 
        If more than one phone number shares the longest total duration,
        the promotion is applied only to the phone number whose
        numerical value is the smallest among these phone numbers.
        '''
     
        for i in data_3:
            
            #getting numerical value of telephone number-number_numerical_value
            number_numerical_value = int()
            
            nnv = i['number']
            nnv = str(nnv)
            nnv = nnv.replace('-', '0')
            
            for nv in nnv:
                number_numerical_value += int(nv)
                
            num_data = {'number':i['number'], 'value':number_numerical_value}
            
            data_4.append(num_data)

    else:
        
        for i in data_3:
            data_4.append(i['number'])
            
    #contains all(or one) number_numerical_value
    data_5 = []
    
    for i in data_4:
        data_5.append(i['value'])

    data_5.sort()
    data_5 = data_5[0]#getting smallest numerical value
    #and now data_5 contains smallest numerical value
    
    #contains number with smallest numerical value
    free_number = None
    
    for i in data_4:
        
        if i['value'] == data_5:
            
            free_number = i['number']
            
    #returns number with free cost of all calls            
    return free_number
            

