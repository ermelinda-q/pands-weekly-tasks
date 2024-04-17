# Programming and Scripting - coding with Python
# Weekly Tasks - Week 8 - matplotlib
# This program displays:
# - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# - a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

# Author: Ermelinda Qejvani


# importing libraries for our project 
# numpy - performs mathematical operations on arrays
# pyplot from matplotlib - used for plotting 2D graphs

import numpy as np
import matplotlib.pyplot as plt


# Building the histogram
# define mean as 'mean', standard deviation as 'standard_dev' and number of values as 'num_of_values' based on the requirements
mean = 5
standard_dev = 2
num_of_values = 1000

# draw random samples from a normal distribution and store values in 'hist_data' 
hist_data = np.random.normal(mean, standard_dev, num_of_values)

# plotting the histogram - data from hist_data, align in the middle, bar color pink, edges in green and label
plt.hist(hist_data, align='mid', color='pink', edgecolor='green', label='Normal Distribution')


# building the plot of the function
# defining a function(h) for our h(x)=x^3 function
def h(x):           # for each given value of x
    return x**3     # return value entered to the power of 3

# defining x_values as an array of evenly spaced values 0-10 using .linspace function
x_values = np.linspace(0, 10)

# defining y_values based on x_values to the power of 3 calling 'h' function defined above.
y_values = h(x_values)

# plotting the function using .plot with x_values, y_values, color black, and label.
plt.plot(x_values, y_values, color='black', label='function $h(x) = x^3$')

# setting the labels for x, y axis, title and legend of histogram and graph.

plt.xlabel(xlabel='Distribution Values / Values of x', fontsize='medium', fontfamily='cursive', color='firebrick')
plt.ylabel(ylabel='Frequency of Distribution Values / Values of h(x)',fontsize='medium', fontfamily='cursive', color='firebrick' )
plt.title(label="Histogram of Normal Distribution and Plot of $h(x) = x^3$\n(with a draggable legend)", fontsize='x-large', fontfamily='cursive', color='firebrick')
plt.legend(fancybox=True, fontsize='small', facecolor='cornsilk', edgecolor='goldenrod', draggable=True, shadow=True)
plt.grid(True, color='olive')

# display 
plt.show()

# https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# https://rowannicholls.github.io/python/graphs/ax_based/histograms.html
# .xlabel, .ylabel, .title, .legend and .grid setting based on https://matplotlib.org/stable/users/explain/quick_start.html
