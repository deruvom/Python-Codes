n=int(raw_input("Size of the array ").strip())
while not (1<=n<=10):
    print ("The size of the array must be in the range [1,10], enter again")
    n=int(raw_input("Size of the array: ").strip())
else: 
     mynewarrint=[]
     myarrint=map(int,raw_input("Enter the elements of the array: ").strip().split(' '))
     for item in myarrint:
             if (0<=item<=100):
                 print sum(mynewarrint)
             else:
                while not (0<=myarrint[:]<=100):
                    print ("The precision of the elements must be in the range [0,10^10], enter again")
                    mynewarrint=map(int,raw_input("Enter the elements of the array: ").strip().split(' '))
                    myarrint[:]=mynewarrint[:]
