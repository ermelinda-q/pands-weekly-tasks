# Programming and Scripting
# Weekly task - Week 6 
# This program reads a floating point number as input and outputs its square root.
# Aim of the program: Creating & working with functions.
# Author: Ermelinda Qejvani


def sqrt(n):                                    # defining a function 'sqrt'
    # creating two variables 'init_val' and 'better'
    init_val = 0.5 * n                          # setting initial value to 0.5  of the given number
    better = 0.5 * (init_val + n/init_val)      # better variable is 0.5 (init_val + number/init_val)
    while better != init_val:                   # the loop will run until 'better' will be equal to 'init_val'
        init_val = better
        better = 0.5 * (init_val + n/init_val)
    return init_val


while True:                                     # creating a loop to check that user is entering a positive value and will run until that happens
    try:
        n = float(input("Please enter a positive number: "))  # n variable will hold the user input value as a float number
    except ValueError:                          # if user enters anything apart from a float number
        print("You entered an invalid value.")  # print message of value error
        continue                                # keep running the loop
    if n < 0:                                   # another condition is to get a positive number so checking if n is negative
        print("You entered a negative number.") # notify the user that the value is  negative number
        continue                                # keep running the loop and to back to try block again
    else:                                       # else means user entered a positive number
        sqrt_value = sqrt(n)                    # call sqrt function created above with the n value from user and assign that number to variable sqrt_value
        break                                   # break the loop 
# Final message to user with input number and with its square root value displayed
print(f"The square root of {n} is approx. {sqrt_value}")


# this is the basic code I used at the start to get number from user input and call sqrt function
# n = float(input("Please enter a positive number: "))  
# print(f"The square root of {n} is approx. " + str(sqrt(n)))     

# I used as a guide the following link
# https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html