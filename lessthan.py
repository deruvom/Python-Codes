def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    newList=[]
    for l in aList:
            if len(l)<4:
                newList.append(l)
    return newList
