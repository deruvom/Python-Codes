def solve(a0, a1, a2, b0, b1, b2):
    a_sum=0
    b_sum=0
    if a0>b0:
        a_sum+=1
    if a1>b1:
        a_sum+=1
    if a2>b2:
        a_sum+=1
    if a0==b0 or a1==b1 or a2==b2:
        a_sum+=0
        b_sum+=0
    if a0<b0:
        b_sum+=1
    if a1<b1:
        b_sum+=1
    if a2<b2:
        b_sum+=1
    print (a_sum,b_sum)
        
solve(3, 4, 5, 5, 6, 7)        