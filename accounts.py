# Programming and Scripting - coding with Python
# Weekly Tasks - Week 3 -  Variables

# Program Title: Reading a bank account and displaying only the last 4 digits
# This program reads in an account number and displays only the last 4 digits
# of the account replacing the rest with X

# This is a revised version of this program using a function(hide_account),
# using .isdigit buildup python function and raise ValueError function from later lessons.

# Author: Ermelinda Qejvani

# defining the hide_account function. This function reads a variable and changes the variable by
# replacing its digits by X, apart from last four digits.
def hide_account(account_number):
    # using multiply sign(*) we are changing each digit of the string to X, appart the last four digits.
    # the variable hidden_account will hold the changed account number/
    hidden_account = 'X' * (len(account_number) - 4) + account_number[-4:]
    return hidden_account

while True:     # while loop will run until condition(input digits from user) is met.
    try:
        # defining variable account_number which will hold input from user.
        account_number = input('Enter your account number: ')  
        # checking if input is digit(our condition for the loop)                
        if not account_number.isdigit(): 
            # error is raised and program continues to run. Loop starts again.
            raise ValueError("Please enter only digits.")  
        # this step will call our hide_account function. Means that user input is digits.
        display_account = hide_account(account_number)     
        # print message and display the in the form of X's and four last digits.
        print("The account number you entered is: ", display_account)
        break  # condition is met, break the loop
    except ValueError as ve:        # print the error message in case of invalid input.
        print(ve)

# The following code is a simple solution if the 'account_number' value was just 10 digits as stated at the start of the task 3.
# print('XXXXXX' + account_number_string[-4:])



