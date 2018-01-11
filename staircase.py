def staircase(n):
    a=[]
    mya=""
    for i in range(n):
        a.append("#"+"#"*i)
        print(a)
        mya+=a[i].rjust(6)+"\n"
    print(mya)
  
    
staircase(6)