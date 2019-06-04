'''
input params:
unic_numbers_dict_array - array of dictionary of unique numbers(numbers_set)
with 0 value of cost and duration of calls for each number (the longest call).

num_all_info_array - array of dictionaries,
each dictionary contains: number, cost and duration of the call.


Returns dictionary which contains the info about all calls
and shows the total cost and duration(in seconds) for each number dialed.
'''

def getInfoNumSum(arrayUniqueMembers, arrayNumAllInfo):
    sumNumInfo = [];
    for u in arrayUniqueMembers:
        data = {'number': u['number'], 'cost' : 0, 'duration':  0};
        for n in arrayNumAllInfo:
            if u['number'] == n['number']:
                data['cost'] += n['cost'];
                data['duration'] += n['duration'];
            else:
                pass
        sumNumInfo.append(data);
    return sumNumInfo;
