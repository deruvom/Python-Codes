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
 #   print n
    
 

####  recursive version
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
            
            else: 
                return False
                 
    
        elif n%2 != 0: # odd length - only one middle char
            # print "middle char in the odd string is: ", middle_char
            
             if n == 1:
               # if char == aStr[:]:
                #    return True
                #else: 
                #    return False
                # shorter : 
                return char == aStr[:]
            
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
                return False
                 
   
             
    else: 
        print "not found"
        return False
  
                 
             
print isIn('e', 'jsd')


##################### SOLUTION #####################



#   # Base case: If aStr is empty, we did not find the char.
#   if aStr == '':
#      return False
#
#   # Base case: if aStr is of length 1, just see if the chars are equal
#   if len(aStr) == 1:
#      return aStr == char
#
#   # Base case: See if the character in the middle of aStr equals the 
#   #   test character 
#   midIndex = len(aStr)/2
#   midChar = aStr[midIndex]
#    print midChar
#   if char == midChar:
#      # We found the character!
#      return True
#   
#   # Recursive case: If the test character is smaller than the middle 
#   #  character, recursively search on the first half of aStr
#   elif char < midChar:
#      return isIn(char, aStr[:midIndex])
#
#   # Otherwise the test character is larger than the middle character,
#   #  so recursively search on the last half of aStr
#   else:
#      return isIn(char, aStr[midIndex+1:])
