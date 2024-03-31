# Programming and Scripting
# Weekly Task - Week 5 
# This program will display the day of the week, date, month, year and
# depending on the day of the week one of the following messages:
# 'Yes, unfortunately today is a weekday!' or 'It is the weekend, yay!'
# Author: Ermelinda Qejvani

import datetime                                         # calling built in module datetime

today_date = datetime.date.today()                      # variable today_date is storing today's date 'datetime.date returns the date without the hours'

current_day = today_date.strftime('%A')                 # current_day is storing the name of the day in full format eg: Monday
current_date = today_date.strftime('%d %B %Y')          # current_date is storing the date, month(in full) and year

print(f"Today is {current_day}, {current_date}")        # output message with the day, date, month and year

if current_day in {"Saturday", "Sunday"}:               # check: if it is Saturday or Sunday
    print("It is the weekend, yay!")                    # output message
else:                                                   # if it is not Saturday or Sunday
    print("Yes, unfortunately today is a weekday!")     # output message
    
