# Programming and Scripting - coding with Python
# Weekly Tasks - Week 2 - Statements
# This program ask the user to enter two amounts in cents, reads in the amounts, adds them and prints out the total amount in cent.
# Print out format @ the end with the euro sign - e.g: 2.22

# Author: Ermelinda Qejvani


first_amount = int(input('Enter your first amount(in cent): '))       # variable 'first_amount'storing(as int) number entered from user input
print(f'The amount you entered is  {first_amount} cent')              # display message with first_amount

second_amount = int(input('Enter your second amount(in cent): '))     # variable 'second_amount' storing(as int) number from user input
print(f'The amount you entered is {second_amount} cent')              # display message with second_amount

total_amount = first_amount + second_amount                           # variable 'total_amount' storing the sum of 2 variables above
total_in_euro = total_amount / 100                                    # variable 'total_in_euro' is storing the value of 'total_amount' divided by 100
                                                                      # as there are 100 cent in 1 euro
print(f'Total amount in cent is: {total_amount} cent')                # display message with total_amount in cent
print(f'Total amount in euro is: €{total_in_euro}')                   # displaying message with total amount in euros


