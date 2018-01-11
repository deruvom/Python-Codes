from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file.  Goodbye!"
#this is not necessary, given that we are writing to a file
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#shorter way:
#target.write("%s \n %s \n %s \n" %(line1,line2,line3)) #this still instert a space when starting the second line
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n") #best

file_again = raw_input('> ')
target2 = open(file_again)

print target2.read()
print "And finally, we close it."
target2.close()