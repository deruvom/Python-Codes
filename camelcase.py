import re
def camelcase(s):
    #print(sum(map(str.isupper, s))+1)
    #count=1
    #for case in s:
    #    if case.isupper():
    #        count+=1
    #print (count)
    #
    mysplit=re.sub(r'([a-z]*)([A-Z])',r'\1, \2',s)
    newsplit=mysplit.split(',')
    print(len(newsplit))




camelcase("saveChangesInTheEditor")