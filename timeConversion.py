import re
import datetime
def timeConversion(s):

    firsth=int(s.split(':')[0])
    lasth=re.split('(\d+)',s.split(':')[-1])
    print(lasth[-1])
    if  lasth[-1] =="PM":
        lasthn=lasth[1]
        newstr=s.replace(s.split(':')[-1],'{:s}'.format(lasthn))
        newstr1=newstr.replace(s.split(':')[0],'{:d}'.format(firsth+12))
        if firsth==12:
            newstr1=newstr.replace(s.split(':')[0],'{:02d}'.format(firsth))
    else: 
        lasthn=lasth[1]
        newstr1=s.replace(s.split(':')[-1],'{:s}'.format(lasthn))
    if  lasth[-1]=="AM":
        newstr=s.replace(s.split(':')[-1],'{:s}'.format(lasthn))
        newstr1=newstr.replace(s.split(':')[0],'{:02d}'.format(firsth))
        if firsth==12:
            newstr1=newstr.replace(s.split(':')[0],'{:02d}'.format(0))



        
    print(newstr1)
     
     



timeConversion("04:59:59AM")