def  oddNumbers(l, r):
    myelarr=[]
    for elem in range(l,r+1):
        if elem%2!=0:
            myelarr.append(elem)
    return myelarr
            
oddNumbers(3,9)