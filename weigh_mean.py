def weigh_mean(n,a,w):
    nom=0
    den=0
    for i in range(n):
                nom+=a[i]*w[i]
                den+=w[i]
                print(nom)
    mymean=round(nom/den,1)
            
    print(mymean)


a=[10,40,30,40,50]
w=[1,2,3,4,5]
weigh_mean(5,a,w)