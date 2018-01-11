import numpy as np
def diagonal_difference(n,a):
       #my_sumf=0
       #my_sumb=0
       #for i in np.diag(a):
       #    my_sumf+=i
       #for j in np.diag(np.fliplr(a)):
       #     my_sumb+=j
       #print abs(my_sumf-my_sumb)
       mysumf=0
       mysumb=0
       for i in range(n):
           mysumf+=a[i][i]
           mysumb+=a[i][n-i-1]
           mydiff=mysumf-mysumb
       print abs(mydiff)
       #print(abs(sum([a[i][i] - a[i][n-i-1] for i in range(n)])))

    
    
diagonal_difference(3,([[11, 2, 4],[4, 5, 6],[10, 8, -12]]))