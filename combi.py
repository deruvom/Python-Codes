# -*- coding: utf-8 -*-
import itertools
import matplotlib.pyplot as plt
import numpy as np


k1=np.arange(-2.0, 3,1)
k2=np.arange(-2.0, 3,1)
k3=np.arange(-2.0, 3,1)
k4=np.arange(-2.0, 3,1)
k5=np.arange(-2.0, 3,1)
k6=np.arange(-2.0, 3,1)
k7=np.arange(-2.0, 3,1)
k8=np.arange(-2.0, 3,1)
k9=np.arange(-2.0, 3,1)


def myfun(a,b,c,d,e): 
    return a-b+c+d+e
    
c = itertools.product(k1,k2,k3,k4,k5)
mylist = []
for element in c:
    mylist.append(myfun(*element))
   # print element
    
#print mylist
#print len(list(itertools.product(k1,k2,k3,k4,k5)))
       
y = lambda x: x+k1+k2+k3+k4+k5
fun_variations = []

for k1,k2,k3,k4,k5 in itertools.product(k1,k2,k3,k4,k5):
    for x in  range(0,6):
        fun_variations.append(y(x))
print fun_variations
 
    
for f in fun_variations:
    
        
        print x+k1+k2+k3+k4+k5
    

#
# y(1)
#f = fun_variations[0]
# for x in range(..):
#    if all([f\(\x\) > 0]):
#         for f in fun_variations:
#    for x in …
# fun_variations = {}
#
#for p1, p2, … in …:
#     fun_variations[
