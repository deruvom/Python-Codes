def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # basic checks 
    
    # 1) strings are equal 
    
    n1 = len(str1)
    n2 = len(str2)
    
    print str1[0:n1]
    print str2[:]
  
    
    # 1) strings are empty
    
    if (str1  == '' or str2  == ''):
        print "warning: you typed in an empty string!"
        return False
        
        
   # 2) strings have different length
    
    if  (len(str1) != len(str2)):
        print "warning: strings have different length!"
        return False
    
   
   # 4) strings have length 1
    
    if ((len(str1)== 1 or len(str2) == 1)  and (str1 == str2)):
        return True
            
    elif (n1 > 1 and str1 == str2):
    
        print "warning: strings are equal!"
        return False
        
   # not recursive 
    #else: 
    #    for i in range(0,n1-1):
    #        if str1[i] == str2[i-1]:
    #            return True

   # start recursion
    
    elif (str1[0] == str2[-1]): 
        print "first and last element are equal:",str1[0],str2[-1]
        #return semordnilap(str1[0:n1-1]+str1[1:n1],str2[-n2:-1])
        return semordnilap(str1[1:n1],str2[-n2:-1])
        # also:
        #return semordnilap(str1[1:],str2[:-1])
    else:
        return False
    

   
        
print semordnilap('cab','bac')

