def divisibleSumPairs(n, k, ar):
    mysum=0
    for i in range(0,n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                print (i,j)
                mysum+=1
    print(mysum)
    

divisibleSumPairs(6,3,[1,3,2,6,1,2])