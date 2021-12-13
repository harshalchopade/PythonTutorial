# importing  module calc.py
#The * symbol used with the from import statement is used to import all the names from a module to a current namespace.
#The use of * has its advantages and disadvantages. If you know exactly what you will be needing from the module,
# it is not recommended to use *, else do so
from Modules import *

print(add(10, 2))

#The from import Statement
#Python’s from statement lets you import specific attributes from a module without importing the module as a whole.

#Example: Importing specific attributes from the module
# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))

##################################################################################################
#Locating Modules
#Whenever a module is imported in Python the interpreter looks for several locations.
# First, it will check for the built-in module, if not found then it looks for a list of directories defined
# in the sys.path. Python interpreter searches for the module in the following manner –

#First, it searches for the module in the current directory.
#If the module isn’t found in the current directory, Python then searches each directory in the shell variable
# PYTHONPATH. The PYTHONPATH is an environment variable, consisting of a list of directories.
#If that also fails python checks the installation-dependent list of directories configured at the time Python
# is installed.

# importing sys module
import sys

# importing sys.path
print(sys.path)