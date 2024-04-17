# Programming and Scripting - coding with Python
# Weekly Tasks - Week 4 - Controlling the flow

# Program Title: Collatz Conjecture Exercise
# This program takes a number(+) from the user and checks if:
#   a) if even the numbers will be divided by 2 
#   b) if odd multipy by 3 and add 1
#   c) the process will continue until the answer is one.
# the numbers will be stored in a list and displayed in the end.

# Author: Ermelinda Qejvani


number_list = []                                                    # creating a list to hold values added by calculations

while True:                                                         # this while loop is created to run the program until the user is entering a positive integer
    try:    
        first_number = int(input("Please enter a positive integer: "))      # this is the first number entered by user assigned to 'first_number' variable
    except ValueError:                                              # calling the build in function to catch a value entered diff from integer
        print("You entered an invalid value.")
        continue                                                    # continue here starts the code from the start 'try'
    if first_number < 0:                                            # if integer entered has a negative value
        print("You should enter a positive value.")                 # print a message
        continue                                                    # and try again
    print(f"The number you entered is: {first_number}")             # this is the first print when a positive integer is entered by user
    
    if first_number == 1:                                               # if user enters one that will be the only value added on the list
        number_list.append(first_number)                                # the program will display 1 and closes
        print(f"Number Sequence is: {number_list}")                     # in Collatz Conjecture when you arrive in number 1 the program will enter in a loop with numbers (1, 4(1+*3+1), 2(4/2), 1(2/2))
    elif first_number > 0:                                              # next condition 'x>0'
        while first_number > 1:                                         # creating a loop with the condition to run while value of number > 1
            number_list.append(first_number)                            # append  the list 'number_list' with the number
            if (first_number % 2):                                      # check if number is odd
                first_number = int(3 * first_number + 1)                # if odd:  multiply by 3 then adding 1
            else:                                                       # else: if number is even
                first_number = int(first_number / 2)                    # devide number by 2
        number_list.append(1)                                           # I had to add number 1 in the end because while first_number >= 1 didn't work
                                                                        # as stated above if number is 1 program enters in a loop and doesn't stop
        print(f"Number Sequence is: {number_list}")                     # print the list of number from the list created from above calculations

    break                                                               # break the while loop and exit the program
