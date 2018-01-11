myarrayfirst=raw_input("Enter the numbers") #this is for entering two or more integers
print myarrayfirst
myarray=map(int, myarrayfirst.split()) #this is for entering two or more integers
print myarray
#myarray=[5,-3,-1]
firstlarg = max(myarray)
allseclarg =[]
#N=len(myarray)
print  'The largest number is', firstlarg
for i in myarray:
    print i
    if i<firstlarg:
            allseclarg.append(i)

                        
seclarg = max(allseclarg)
print 'The second largest number is', seclarg

    


# if I am asked to find the second largest number, it is sufficient to store all numbers
#which are smaller than the largest in a new array and then find the maximum among these numbers
#
#m=0
#for i in range(len(myList)):
# if m<myList[i]:
#  m=myList[i]