
n=int(raw_input("Size of the array ").strip())
myarrint=map(int,raw_input("Give me the array ").strip().split(' '))



print myarrint
posarr=[]
negarr=[]
zeroarr=[]
for item in myarrint:
    print item
    if item>0:
        posarr.append(item)
    if item<0:
        negarr.append(item)
    if item==0:
        zeroarr.append(item)
print len(posarr)
posfrac= len(posarr)/float(len(myarrint))
negfrac= len(negarr)/float(len(myarrint))
zerofrac= len(zeroarr)/float(len(myarrint))
print ('%.6f' % posfrac)
print ('%.6f' % negfrac)
print ('%.6f' % zerofrac)

