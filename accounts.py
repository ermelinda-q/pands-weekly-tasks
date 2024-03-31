# Programming and Scripting (coding with Python)
# Weekly Task - Week 3 -  Statements

# Program Title: Reading a bank account and displaying only the last 4 digits
# This program reads in an account number and displays only the last 4 digits
# of the account replacing the rest with X

# Author: Ermelinda Qejvani

account_number = int(input('Enter your account number: '))                  # variable account_number will hold an integer value from user input
account_number_string = str(account_number)                                 # convert to string and hold it to account_number_string variable

account_number_length = len(account_number_string)                          # getting the length of the string 'account_number_string'

if account_number_length > 4:               # checking the length of account: if > 4
    # multiplying by X a string (part of string till the 4 digit from the end substitutes them all by X)
    # display_account_number is a variable that holds the new string modified 
    display_account_number = 'X' * (account_number_length -4) + account_number_string[-4:] 
    # print message with the account number modified
    print('The account number you entered is: ', display_account_number) 
else:           # if account number is less then four digits, print the account number as it is entered by user
    print('The account number you entered is too short\nThe account number you entered is: ',account_number_string )


# The following code is a simple solution if the 'account_number' value was just 10 digits as stated at the start of the task 3.
# print('XXXXXX' + account_number_string[-4:])



