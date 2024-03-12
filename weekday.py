# Programming and Scripting
# Week 5 weekly tasks
# This program will display the day of the week and
# a message the following message:
# 'Today is (whatever week day).'
# 'Whatever week day' is a weekday!'
# or' 
# 'Today is (whatever week day)'
# 'It is the weekend, yay!'
# Author: Ermelinda Qejvani

from datetime import datetime # calling built in module datetime

today_date = datetime.today()  # with this we are gettin first the date and time - full info about the day

# print(today_date)  ---------- I used this code to check that the above code was working or not

today_name = str(today_date.strftime('%A'))   # reading the day from today_date as a string

if today_name != ["Saturday", "Sunday"]: # checking if weekend
    print(f"Today is: {today_name}")           # displaying information
    print("Yes, unfortunately today is a weekday!")
else:   # if weekend
    print(f"Today is: {today_name}")
    print(f"It is the weekend, yay!")