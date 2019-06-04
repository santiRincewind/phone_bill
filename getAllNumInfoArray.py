from getCost import getCost

'''
retrieves all data separated by ,
'''
def get_massive_all(data):
    data_a = [];
    for i in data:
        i = i.split(',');
        data_a.append(i);      
    return data_a;
'''
Converts a given string and returns an array of dictionaries,
each dictionary contains: number, cost and duration of the call.
'''
def getAllNumInfoArray(strFile):
    data = strFile.split('\n');
    a = get_massive_all(data);
    num_all_info_array = [];      
    for i in a:      
        cost = int();
        t = i[0];
        h, m, s = t.split(':');
        duration = (int(h) * 3600 + int(m) * 60 + int(s));      
        cost = getCost(duration);
        dt = {'number' : i[1], 'cost' : cost, 'duration':  duration};
        num_all_info_array.append(dt);
    return num_all_info_array;

