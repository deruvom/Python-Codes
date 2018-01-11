
myarray=[1,0,2]
firstlarg = max(myarray)
allseclarg =[]
N=len(myarray)
print  'The largest number is', firstlarg
j=range(1,N)
for i in myarray:
    if i<firstlarg:
            allseclarg.append(i)

                        
seclarg = max(allseclarg)
print 'The second largest number is', seclarg

    


# if I am asked to find the second largest number, it is sufficient to store all numbers
#which are smaller than the largest in a new array and then find the maximum among these numbers
