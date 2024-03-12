# Programming and Scripting
# Week 6 weekly tasks
# This program reads a floating point number as input and outputs its square root.
# Aim of the program: Creating & working with functions.
# Author: Ermelinda Qejvani

def sqrt(n): # defining a function 'sqrt'
    # creating two variables 'init_val' and 'better'
    init_val = 0.5 * n                     # setting initial value to 0.5  of the given number
    better = 0.5 * (init_val + n/init_val)   # better variable is 0.5 (init_val + number/init_val)
    while better != init_val:              # the loop will run until 'better' will be equal to 'init_val'
        init_val = better
        better = 0.5 * (init_val + n/init_val)
    return init_val
n = float(input("Please enter a positive number: "))
print(f"The square root of {n} is approx. " + str(sqrt(n)))

# I used as a guide the following link
# https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html