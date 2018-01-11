#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.

s = 'bobiidehbigibobbob'

ntime=0
recur=0
string = 'bob'
for letters in range(0,len(s)-1):
    if string in s: 
        ntime=+1
        recur+= ntime

        print s[letters:letters+len(string)]
#recur = s.count('bob')
#print ('Number of times bob appears is:' + str(recur))

#SOLUTION
#numBobs = 0
#for i in range(1, len(s)-1):
#    if s[i-1:i+2] == 'bob':
#        numBobs += 1