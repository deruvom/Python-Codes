def quart(n,k):
    mysorted=sorted(k)
    if len(k)%2==0:
        median=(mysorted[(len(k)-2)//2]+mysorted[((len(k)-2)//2)+1])/2
        q1=mysorted[0:(len(k)-2)//2+1]
        med_q1=(q1[(len(q1)-2)//2]+q1[((len(q1)-2)//2)+1])/2
        qu=mysorted[((len(k)-2)//2)+1:len(k)+1]
        qu_med=(qu[(len(qu)-2)//2]+qu[((len(qu)-2)//2)+1])/2
        
    else:
        median=mysorted[(len(k)-1)//2]
        q1=mysorted[0:(len(k)-2)//2+1]
        qm=mysorted[((len(k)-2)//2)+1]
        qu=mysorted[((len(k)-2)//2)+2:len(k)+1]
        med_q1=(q1[(len(q1)-2)//2]+q1[((len(q1)-2)//2)+1])/2
        qu_med=(qu[(len(qu)-2)//2]+qu[((len(qu)-2)//2)+1])/2
   

    print(round(med_q1))
    print(round(median))
    print(round(qu_med))
    

        

    
    




n=int(input())
k=list(map(int,input().strip().split(' ')))
quart(n,k)