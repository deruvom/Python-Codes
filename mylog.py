def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''

    mylog=0
    conditions=[b<2,x<=0,type(b) is not int,type(x) is not int,x<b]
    if any(conditions):
            print ("One or more of these conditions true: b<2,x<=0,type(b) is not int,type(x) is not int,x<b")
            return 0
    else:
        for c in range (0, x):
            if int(b**c)<=x:
                mylog=c
        return mylog