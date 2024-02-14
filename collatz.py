# Programming and Scripting (coding with Python)
# Weekly Task 04

# Program Title: Collatz Conjecture Exercise
# This program takes a number(+) from the user and checks if:
# a) if even the numbers will be divided by 2 
# b) if odd multipy by 3 and add 1
# c) the process will continue until the answer is one.
# the numbers will be stored in a list and displayed in the end.

# Author: Ermelinda Qejvani

number_list = []  # list of numbers created by calculations

first_number = int(input("Please enter a positive integer: ")) # this is the first number entered by user

if first_number == 1:
    number_list.append(first_number)
    print(f"Number Sequence is: {number_list}")
elif first_number > 0:
    while first_number > 1:
        number_list.append(first_number) # adding number to the number_list
        if (first_number % 2):       # if number is odd
            first_number = int(3 * first_number + 1)  # odd number multiply by 3 then adding 1
        else:       # number is even
            first_number = int(first_number / 2)
    number_list.append(1) # I had to add number 1 in the end because while first_number >= 1 didn't work
    print(f"Number Sequence is: {number_list}")

else:
    print("Invalid number! \nGoodbye!")

