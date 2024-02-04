# Week 2 - weekly tasks
# This program ask the user to enter two amounts in cents, reads in the amounts, adds them and prints out the total amount 
# Print out format int the end: €2.22

# Author: Ermelinda Qejvani


first_amount = int(input('Enter your first amount(in cent): '))  # asking the user to enter their first cent amount
print(f'The amount you entered is  {first_amount} cent')              # confirming the amount entered

second_amount = int(input('Enter your second amount(in cent): '))        # asking the user to enter their second amount.
print(f'The amount you entered is {second_amount} cent')             # displaying the second amount entered.

total_amount = first_amount + second_amount                     # defining how to get total amount in cent by adding both amounts
total_in_euro = total_amount / 100                              # defining how to convert cents to euros

print(f'Total amount in cent is: {total_amount} cent')               # displaying total amount in cents
print(f'Total amount in euro is: €{total_in_euro}')             # displaying total amount in euros
