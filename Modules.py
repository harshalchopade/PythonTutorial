#A Python module is a file containing Python definitions and statements.
# A module can define functions, classes, and variables.
# A module can also include runnable code. Grouping related code into a module makes the code easier to
# understand and use. It also makes the code logically organized.

def add(x, y):
    return (x + y)


def subtract(x, y):
    return (x - y)

#Import Module in Python –  Import statement
#We can import the functions, classes defined in a module to another module using the import statement in some other Python source file.
#Syntax - import module

#When the interpreter encounters an import statement, it imports the module if the module is present in the
# search path. A search path is a list of directories that the interpreter searches for importing a module.
# For example, to import the module calc.py, we need to put the following command at the top of the script.
#Note: This does not import the functions or classes directly instead imports the module only.
# To access the functions inside the module the dot(.) operator is used.

