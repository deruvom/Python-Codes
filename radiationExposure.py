from scipy import arange
import numpy
import pylab


    
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    
    #n_rects = (stop - start)/step
    #
    #area = 0
    #print n_rects
    #for i in numpy.arange(start, (start + n_rects)):
    #    area += f(i) * step
    #    print area, i 
    #    
   # without for loop (range is valid only for int, so I would need arange for float): 

    result = 0
    while(start <  stop):
        result += f(start) * step
        start += step
    return result
    
    # recursive version
 #   if (stop - start) <= 0: # comparing floats
 #       return 0
 #   else:
 #       return f(start)*step + radiationExposure(start+step,stop,step)
 #
      
x = numpy.linspace(0,100,10)
y = f(x)
pylab.plot(x,y)
pylab.show()
print radiationExposure(40,100,1.5)