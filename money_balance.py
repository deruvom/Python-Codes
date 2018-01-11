#Write a program to calculate the credit card balance after one year if 
#a person only pays the minimum monthly payment required by the credit card company each month.
#A summary of the required math is found below:
#
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#
#
#The following variables contain values as described below:
#
#balance - the outstanding balance on the credit card

#annualInterestRate - annual interest rate as a decimal
#
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#
#For each month, calculate statements on the monthly payment and remaining balance, 
#and print to screen something of the format:

#Month: 1
#Minimum monthly payment: 96.0
#Remaining balance: 4784.0
#Be sure to print out no more than two decimal digits of accuracy - so print
#
#Remaining balance: 813.41
#instead of
#
#Remaining balance: 813.4141998135 
#Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:
#
#Total paid: 96.0
#Remaining balance: 4784.0

#Note that the grading script looks for the order in which each value is printed out. We provide sample test cases below; 
#we suggest you develop your code on your own machine, and make sure your code passes the sample test cases, 
#before you paste it into the box below.

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
annual_paid=0

for month in range (1,13):
    print 'Month:', month
    min_monthly_pay = balance * monthlyPaymentRate 
    
    print 'Minimum monthly payment: ',round(min_monthly_pay,2)
    monthly_interest_rate = annualInterestRate/12.0
   # print 'Monthly interest rate: ', round(monthly_interest_rate,2)
    monthly_unpaid_bal=balance-min_monthly_pay
   # print 'Monthly unpaid bal: ', round(monthly_unpaid_bal,2)
    res_balance =monthly_unpaid_bal + (monthly_interest_rate * monthly_unpaid_bal)
    print 'Remaining balance: ', round(res_balance,2) #, ("%.2f" % res_balance)
    
    balance=res_balance
    
    annual_paid+=min_monthly_pay
    
print 'Total paid per year: ', round(annual_paid,2)
    
print 'Balance at the end of the year: ', round(balance,2)
