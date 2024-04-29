## Programming and Scripting - Weekly Tasks

##### *Author: Ermelinda Qejvani*

This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***
### About

This repository contains all weekly tasks required for 'Programming and Scripting' module in [Hdip in Science in Computing in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics) @ [ATU](https://atu.ie).

All efforts are made to follow as much as possible [Style Guide for Python Code](https://peps.python.org/pep-0008/) while working in these tasks.

Here you can find:

- All .py files for each week.
- File [weekly-tasks.ipynb](/weekly-tasks.ipynb) - containing all .py files in one jupyter notebook.
- .gitignore file.
- this README file that contains requirements for each weekly task and references used.


***
### Get Started

To run the files stored in this repository you will need to download and install in your computer the following apps:

- [Anaconda](https://www.anaconda.com/) - open-source platform that allows you to write and execute code in Python. A guide how to install Anaconda in your computer can be found [here](https://docs.anaconda.com/free/anaconda/install/index.html).
- [Visual Studio Code](https://code.visualstudio.com/) - source code editor for developers. With Visual Studio Code you can open and run all python files(ending with .py) and [weekly-tasks.ipynb](/weekly-tasks.ipynb) file created with Jupyter Notebook. A guide how to install and setup Visual Studio Code in your computer can be found [here](https://code.visualstudio.com/learn/get-started/basics).
- [Git](https://git-scm.com/downloads) - will help you to download a copy of this repository in your local machine. Installation guide can be found [here](https://github.com/git-guides/install-git).

To make a copy of this repository in your computer/local machine run the following command:

```
git clone https://github.com/ermelinda-q/pands-weekly-tasks.git
```

***
### Description of work 
***

__Week 1__

This is my first program in python. It prints out 'Hello World'

Filename: [helloworld.py](./helloworld.py)

***

__Week 2 - Statements__

Filename: [bank.py](./bank.py)

Task: Write a program that should:
1. Prompt the user and read in two money amounts (in cent).
2. Add the two amounts.
3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 

References:
1. Week 2 lecture by Andrew Beatty.
2. [Python's F-String](https://realpython.com/python-f-strings/).

***

__Week 3 - Variables__

Filename: [accounts.py](./accounts.py)

Task: Write a program that:
1. Reads in a 10-character account number.
2. Outputs the account number with only the last 4 digits and the first 6 digits replaced with X's.
3. Modify the program to deal with account numbers of any length.

References:
1. Week 3 lecture on Variables by Andrew Beatty.
2. [Modify Strings](https://www.w3schools.com/python/python_strings_modify.asp).
3. [Conditional Statements in Python](https://realpython.com/python-conditional-statements/).

***

__Week 4 - Controlling the flow__

Filename: [collatz.py](./collatz.py)

Task: Write a program that:
1. Asks the user to input any positive integer
2. Outputs the successive values of the following calculations.
    - At each step calculate next value by taking the current value and:
        1. if even divide it by two,
        2. if odd multiply it by three and add one.
3. Have the program end if the current value is one.

References:
1. [YouTube video on the collatz conjecture(Veritasium)](https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s).
2. [Collatz conjecture sequence](https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence).
3. [Using 'while True' function](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response).

***

__Week 5 - Data__

Filename: [weekday.py](./weekday.py)

Task: Write a program that outputs whether or not today is a weekday.

This program will display:
1. the day of the week, date, month, year
2. Depending on the day of the week, it will also display one of the following messages:
    - 'Yes, unfortunately today is a weekday!' or 
    - 'It is the weekend, yay!'

References:
[Python datetime.strftime()](https://www.programiz.com/python-programming/datetime/strftime)

***

__Week 6 - Functions__

Filename: [squareroot.py](./squareroot.py)

Task: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

This program will:
1. Create my own function called sqrt() that finds the square root of the float number.
2. Should be based on Newton's method of estimating square roots.

References: 
[Newton's Method](https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html)

***

__Week 7 - Files__

Filenames: [es.py](./es.py), [week7.txt](./week7.txt)

Task: This program reads a text file and outputs the number of e's it contains.
1. The file name 'week7.txt' should be given as a second argument in command line after the es.py file.
2. We need to check the length of the arguments from command prompt.
3. The right user entry should be 'python es.py week7.txt'.

References:
1. [Counting the number of times a letter appear in a text file](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python).
2. [Read a file from the command line in Python](https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python).


***

__Week 8 - Looking ahead__

Task: This program displays:
1. a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
2. a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

References:
1. [Plotting normal distribution over histogram](https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/).
2. [Histograms](https://rowannicholls.github.io/python/graphs/ax_based/histograms.html).
3. .xlabel, .ylabel, .title, .legend and .grid setting based on [matplotlib API reference](https://matplotlib.org/stable/api/matplotlib_configuration_api.html).

***
## End
