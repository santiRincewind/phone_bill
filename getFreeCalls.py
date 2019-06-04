'''
This Function returns the duration formatted 
'''
def setTimeFormat(duration):
    num=duration;
    hor=(int(num/3600));
    minu=int((num-(hor*3600))/60);
    seg=num-((hor*3600)+(minu*60));
    strDurationFormatted=str(hor)+"h "+str(minu)+"m "+str(seg)+"s";
    return strDurationFormatted;
'''
This function returns the collection with the cost of free calls updated
'''
def getFreeCalls(theFreeNumber, target):
    #target - where need to made free calls for numbers
    for i in target:
        #print(str(hor)+"h "+str(minu)+"m "+str(seg)+"s");
        duration=setTimeFormat(int(i['duration']));
        i['duration']=duration;
        if i['number'] == theFreeNumber:
            i['cost'] = 0;
            i['duration']=duration+" THE FREE PROMOTION APPLIES TO THIS NUMBER"
    return target;
