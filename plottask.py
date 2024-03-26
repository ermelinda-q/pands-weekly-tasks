# Programming and Scripting - Weekly Tasks
# Week 8
# This program displays:
# - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# - a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

# Author: Ermelinda Qejvani
# basic formula
'''
# https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 
import statistics 

x_axis = np.arange(-30, 30, 0.1)

mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))

plt.show()

'''
# https://rowannicholls.github.io/python/graphs/ax_based/histograms.html

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Create a normal distribution probability density function (PDF) with mean 5,
# standard deviation 2 and running from 45 to 155. It will consist of 1,000
# points to ensure it looks smooth when plotted.
x = np.linspace(45, 155, 1000)
mu, sigma = 5, 2
normal_pdf = norm.pdf(x, loc=mu, scale=sigma)

# Plot
ax = plt.axes()
ax.plot(x, normal_pdf)
ax.set_title('Probability Density Function of a Normal Distribution')
ax.set_ylabel('Probability Density')
ax.set_xlabel('IQ Score')