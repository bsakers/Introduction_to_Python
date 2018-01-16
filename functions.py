#as noted previously, to define a function we use 'def'
#after the function is defined, a ":" is required to set the code
def my_function():
    print "we\'re inside the function"
my_function()


#functions can call upon other functions
def fun_one(a):
    return a * 5

def fun_two(b):
    return fun_one(b) + 10

print fun_two(6)


def cube(number):
	return number * number * number
def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
  	return False


#Name errors. NameError: name 'XXXX' is not defined. Means you called XXXX function, which hasn't been defined
#This error often occurs when we try something like sqrt(25). 'sqrt' isn't defined naturally in Python
#That said, we can import the 'math' module. This is called a generic import. This would now look like..
import math
print math.sqrt(25)
#However, using math. over and over is redundent. We can import only the functions we need
from math import sqrt
print sqrt(25)
#Lastly, we can bypass both with the following:
from math import *
print sqrt(25)
#BE CAREFUL WITH THE ABOVE THOUGH! It's easy to get overlapping function names. Use option 1 or 2
#To see all of the imported function, we can:
import math
everything = dir(math)
print everything

#some common functions built into python! (max, min, absolute)
print max(1, 3.21, 5, -5)
print min(1, 3.12, -17, 42)
print abs(-14)
#can also use 'type' to find the class of the argument
print type(14)
print type(3.2222)
print type("Like Tears In The Rain")

def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return "Not a number (neither integer nor float)"
print distance_from_zero(-104.33)

#function with more than one argument
def add_function(x, y):
    return x + y
