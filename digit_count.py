def count_digit(t):

#t = int(input().strip())
#for a0 in range(t):
    for n in t:
        mycount=0
        for d in str(n):
            digit=int(d)
            if digit!=0:
                if n%digit==0:
                    mycount+=1
        print(mycount)
            
            
count_digit([12,10412])