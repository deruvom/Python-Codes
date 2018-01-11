def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
        
# testList = [1, 4, 8, 9]
#
def  minus(a):
    if a < 0: 
        return a * (-1)
    else:
        return a


testList = [1, -4, 8, -9]


#applyToEach(testList, minus)

# testList = [2, -3, 9, -8]

def plusone(a):
    return a +1
    
# applyToEach(testList, plusone)   

 
# testList = [1, 16, 64, 81] 

def byfour(a):
        return a**2

applyToEach(testList, byfour) 
        
    