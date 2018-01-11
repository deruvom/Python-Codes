#import random 
#
#def binarysearch(a,b):
#
#    target= random.randint(a,b)
#    print target
#    myguess= ((a+b)/2)
#    print myguess
#    if a <0 or b<0:
#        raise ValueError
#    while myguess is not target:
#            if myguess < target:
#                a = myguess+1
#                myguess= ((a+b)/2)
#                print ("The new guess if the guess was too low is",myguess)
#            elif myguess > target:
#                b = myguess -1 
#                myguess= ((a+b)/2)
#                print ("The new guess if the guess was too high is",myguess)
#    else:
#            print ("Found it",myguess,target)
#        
#    return myguess
#    
#binarysearch(1,100)
def binarysearch(target,ar):
    myguess=len(ar)/2
    while myguess is not target:
        if myguess>target:
            myguess=(len(ar)-myguess)/2
            print ("The new guess if the guess was too low is",myguess)
        elif myguess<target:
            myguess=(0+myguess)/2
            print ("The new guess if the guess was too high is",myguess)
    print ("Found it",myguess,target)
        
binarysearch(3,[0,3,4,5,6,7])           