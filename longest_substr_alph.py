#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
#Longest substring in alphabetical order is: abc
#For problems such as these, do not include raw_input statements or define the variable s in any way. 
#Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. 
#If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
#
#Note: This problem is fairly challenging. We encourage you to work smart. 
#If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
#If you have time, come back to this problem after you've had a break and cleared your head.

s = 'azcbobobegghakl'
orderi=[] #test
orderj=[] #best


for i in range(len(s)-1):
    if len(orderi) > len(orderj): #len(test>=best)
               orderj=orderi #best=test
    if (s[i]<=s[i+1]):
           orderi.append(s[i])
           orderi.append(s[i+1])
            
    else:
           orderi=[]  
           
           
print orderj

#for j in range(len(orderi)-1):
for j in range(0,4): # need to make this automatic but I can't

                if orderj[j]==orderj[j+1]:
                  # del orderi[j]
                   orderj.remove(orderj[j])
   
print orderj
joined= ''.join(orderj)
print joined



print "Longest substring in alphabetical order is:", joined



#
#test = s[0]      # seed with first letter in string s
#best = ''        # empty var for keeping track of longest sequence  
#
#for n in range(1, len(s)):    # have s[0] so compare to s[1]
#    if len(test) > len(best):
#        best = test
#    if s[n] >= s[n-1]:
#        test = test + s[n]    # add s[1] to s[0] if greater or equal
#    else:                     # if not, do one of these options 
#        test = s[n]
#
#print "Longest substring in alphabetical order is:", best
