import math

def st_dev(n,k):
    sqerr=0
    mean=sum(k)/len(k)
    for i in range(n):
        sqerr+=pow(k[i]-mean,2)
    stdev=round(math.sqrt(sqerr/n),1)
    print (stdev)
        
    
    