def lenIter(aStr):
     '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
  
# iterative call
     length = 0
     for c in aStr: 
        length = length + 1 
    
     return length

#recursive 
    
def lenRecur(aStr):
    
    
    if aStr == '': # empty string
        return 0
   
    
    #  If the string is not zero-length, then remove the first
    #  character and the length is 1 + the length of the rest of the string
    return 1 + lenRecur(aStr[1:])     
    

     
print lenIter('a3dje')

print lenRecur('a3dje')

print len('a3dje')