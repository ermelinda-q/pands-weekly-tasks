# Programming and Scripting (coding with Python)
# Weekly Task 03

# Program Title: Reading a bank account and displaying only the last 4 digits
# This program reads in an account number and displays only the last 4 digits
# of the account replacing the rest with X

# Author: Ermelinda Qejvani

# 'account_number' is the account number entered by user - integer format
account_number = int(input('Enter your account number: '))

# reading the 'account_number' as a string
account_number_string = str(account_number)

# 'acount_number_length' is a variable to get the length of the number entered through 'account_number_string'
account_number_length = len(account_number_string)

# account number can be any length so I'm using 'if, else' function to check the length first:

if account_number_length > 4: # checking if account number is greater than 4 digits
    # creating a variable that will add an 'X' to all digits until the last 4 ones and then will display 
    # just the four digits of account_number_string(it counts from the last digit: -1, -2, etc)
    display_account_number = 'X' * (account_number_length -4) + account_number_string[-4:]
    print('The account number you entered is: ', display_account_number)   # print message + the value of 'display_account_number' value
else:           # if the 'account_number_length'is 4 or less digits
      print('The account number you entered is: ',account_number_string )


# The following code is a simple solution if the 'account_number' value was just 10 digits as stated at the start of the task 3.
# print('XXXXXX' + account_number_string[-4:])



