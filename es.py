# Programming and Scripting
# Weekly task - Week 7 - Files
# This program reads a text file and outputs the number of e's it contains.
# file to read is week7.txt - this file is read by the program as an argument from command line.

# letter_frequency function based on:  https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

# Author: Ermelinda Qejvani

import os       # calling 'os' module to check location of the file
import sys      # calling 'sys' module to access command line arguments

# the file name 'week7.txt' should be given as a second argument in command line after the es.py file
# first we check the length of the argument read on the command line
# in order for the program to read how many e's are in the file be two arguments:
# 1. es.py - our program file
# 2. week7.txt - file to read

def letter_frequency(fileName, letter):     # creating a function 'letter_frequency' to read a file and the letter we will assign.
        with open(FILENAME, 'r') as f:      # open file stored on variable FILENAME(see code below) in read only mode as f
            text = f.read()                 # read the file
            count = 0                       # set counter to 0
            for char in text:               # variable char will be holding the requested letter
                if char == letter:          # if char is equal to the letter
                    count +=1               # count is increased by one
            return count                    # return the last number counted

if len(sys.argv) < 2:                       # checking the length of arguments entered by user if no file entered (file is the second argument)
    print("Please add the filename as an argument on the command line.")  # print message
    exit()                                  # exit program
elif len(sys.argv) > 2:                     # I'm putting this check to make sure that only two arguments are entered
    print("Too many arguments. Please try to run the program again with only two arguments")
    exit()  
elif len(sys.argv) == 2:                    # if two arguments entered in command line
                                            # we are reading second argument [0 for program name, 1 for text file]
    FILENAME = sys.argv[1]                  # variable FILENAME will hold the argument value(filename entered from user)
    if not os.path.exists(FILENAME):        # checking if the file doesn't exist in the same directory as the program file
        print("The file does not exist!")   # print message
        exit()                              # exit the program
    else:                                   # if the file exists
        print(f"Reading file: {FILENAME}")  # print message that the file entered is being processed by the program
        # print the message with total numbers of e letters after calling function 'letter_frequency' created at the start of program
        print(f"There are {letter_frequency(FILENAME, 'e')} 'e' letters in the text") 
    exit()

    