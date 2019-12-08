# MACHINE PROBLEM 1
# Python program to graph the values of f(n) from 0 to 99.

# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB
# matplotlib is a plotting library for Python and NumPy

# importing the matplotlib.pyplot
import matplotlib.pyplot as plot

# importing the numpy
import numpy as np

# creating numeric sequence f with 0 values, and size of 100
f= np.linspace(0,0,100)

# loop for x in the sequence 0 to 100
for x in range(0,100):
    
     
    # boolean expression where it tests if x is less than 9
    a= int(x<=9)
    
    # boolean expression where it tests if x is greater than or equal to 10
    b= int(x>=10)
    
    # the value that is obtained from a & b is 1 or 0 because of int
    
    
    # the boolean integer result from b is incorporated to the given piecewise function [f(n-10)]
    # when the boolean expression is 0 or false, the function will be invalid and will not run
    c= (x*b)-10
    

    # f is a variable with the index (x), changing every iteration
    # the piecewise function is added, while incorporating the boolean expression
    # when the boolean expression is false, the certain function will be disregard because it is multiplied to 0
    # the boolean expression results in true or false so int should be used
    f[x]= int(x <= 9)*(((x*(a))**2)-7) + int(x >= 10)*(f[c])
    
    # plotting the values of x as 0 to 100, and y as f, using stem
    # use_line_collection=True gives a very large performance boost to displaying and moving stem plots
    plot.stem(range(0,100),f, use_line_collection=True)
    
    # putting labels
    plot.xlabel('n(0-99)')
    plot.ylabel('f(n)')
    
    # putting title
    plot.title('Machine Problem 1')
    
