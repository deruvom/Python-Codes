def fact(n):
    """assumes that n is an int >0, return n! """
    
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

# recursive version 

def factR(n):
    """assumes that n is an int >0, return n! """
    
    if n == 1:
        return n
    return n* factR(n-1)
   


    
fac = fact(3)
print fac

fac2 = factR(3)
print fac2