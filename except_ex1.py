#def FancyDivide(numbers,index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError, e:
#        print "-1"
#    else:
#        print "1"
#    finally:
#        print "0"


def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
            return 0
    
      
      
print FancyDivide([0,2,4],0)