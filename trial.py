s='ciao'
i=0

while i< len(s): 
    for item in s:
      if item == 'a' or 'o':
        i=i+1

print i