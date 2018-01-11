def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    aStr = sorted(aStr)
    print aStr[:]
    n = len(aStr)
    print n
    
    
    #if n%2 == 0: # even length: compare both to the middle left and middle right char
        #if (char == middle_char_left or char == middle_char_right):
        #    print "found it!", char
        #   # return True
        #    
        #elif (char < middle_char_left): 
        #    check lower half
        #elif (char > middle_char_right): 
        #    check upper half
        #    
        #    print "wrong"
        #    return False
     #elif n%2 != 0: # odd length - only one middle char
     #   if char == middle_char:
     #       print "found it!", char
     #       return True
     #   else: 
     #       print "wrong"
     #       return False
     #   print "middle char in the odd string is: ",middle_char
     #   
    
 

#### shorter and recursive version
    if n > 0: 

        middle_char_left = aStr[(n/2)-1]
        middle_char_right = aStr[(n/2)]
        middle_char = aStr[(n-1)/2]

        if n%2 == 0: # even length: compare both to the middle left and middle right char          
            print "middle chars in the even string are: ", middle_char_left,middle_char_right
        #return (char == middle_char_left or char == middle_char_right)
        
              
            if char == middle_char_left or char == middle_char_right:
                print "found it"
                return True 
                 
        
            if (char < middle_char_left and char < middle_char_right):
                print "checking the lower half in the even string"
                return isIn(char,aStr[0:n/2-1])
       
            elif (char > middle_char_left and char > middle_char_right):
                print "checking the upper half in the even string"
                return isIn(char,aStr[n/2:n+1])
        
    
        elif n%2 != 0: # odd length - only one middle char
             print "middle char in the odd string is: ", middle_char
            
             if char == middle_char:
                 print "found it"
                 return True 
             
             if char < middle_char:
                 print "checking the lower half in the odd string"
                 return isIn(char,aStr[0:(n-1)/2])
              
             if char > middle_char:
                 print "checking the upper half in the odd string"
                 return isIn(char,aStr[n/2:n+1])
             
    else: 
        print "not found"
        return False
  
                 
             
print isIn('a','fifgahc')
