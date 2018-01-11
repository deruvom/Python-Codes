y=raw_input("Please think of a number between 0 and 100")

x = 100.0

epsilon = 0.01
print "Please think of a number between 0 and 100"

x = 100.0

epsilon = 0.01
low = 0.0
high = x
ans = int((high + low)/2.0)
while ans in range(0,100):
    print ("Is your secrect number " + str(ans) + "?")
    choice=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
   # choice = raw_input().lower()
    if (choice == 'l'):
        low = ans
        ans = int((high + low)/2.0)
    elif (choice == 'h'):
        high = ans
        ans = int((high + low)/2.0)
    elif (choice == 'c'):
        print ("Got it! Your secret number was: " + str(ans))
        break
    elif (choice != 'l' or 'h' or 'c'):
        print ("Sorry, did not understand your input")

   