def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

#iterative code

    c = min(a,b)
    if (int(a) and int(b)) > 0:
        while c > 0: 
            if a%c == 0 and b%c == 0: 
                return c
            else:
                c -= 1 
               
    return c
     
     
print gcdIter(9,12)

# recursive code 
    #c = 1
    #divisor = []
    #d = min(a,b)
    #print d
    #if int(a) and int(b) > 0:
    #    while c <= d: 
    #        if a%c == 0 and b%c == 0: 
    #            divisor.append(c)  
    #        c += 1 
    #        
    #return max(divisor)
     

# 2nd recursive code - Euclid algorithm

def gcdRecur(a,b):

    if (int(a) and int(b)) >= 0:
        if b == 0: 
            return a
        else: 
               # if a%c == 0 and b%c == 0: 
            return  gcdRecur(b, a%b)

print gcdRecur(9,12)
