import sys

def sumarray(length,myarr):
    mysumarr=0
    for i in range(0,length):
        mysumarr+=myarr[i]
    return mysumarr
        
        
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print sumarray(n,arr)

