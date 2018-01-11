def birthdayCakeCandles(n, ar):
    mysum=0
    mymax=max(ar)
    for i in ar:
            if i>=mymax:
                mysum+=1
    
    print(mysum)
            
            
birthdayCakeCandles(4, [1,2,2,4]) 
            