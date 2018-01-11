def iterPower(base,exp):
    """ 
    base: int or float
    exp: int >= 0
    
    returns: int or float, base^exp
    """

    result = 1
    while exp > 0:
        exp = exp - 1
        result *= base
    return result

power = iterPower(2,4)
print power

# recursive version


def recurPower(base, exp):
    if exp <= 0:
        return 1
    
    return base * recurPower(base, exp-1)



print recurPower(2,4)

def recurPowerNew(base,exp):
     if float(exp) == 0:
        return 1.0
     elif float(exp) < 0: 
         print "warning: the exp can only take values > 0"
         return 1.0
     if float(exp) > 0 and float(exp)%2 == 0:
        # return base * recurPower(base, exp-1/exp-1)
         return recurPowerNew(base*base, exp/2)
     if float(exp) > 0 and float(exp)%2 != 0:
        return float(base * recurPowerNew(base, exp-1))
    
print recurPowerNew(-9.96,5)


         