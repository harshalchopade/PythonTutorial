#  __name__
#In python we use double __ .
#


#print(__name__) #o/p __main__

#What is main
#If you are coming from c,c++ or java background we know that main is starting point of execution.
#Same goes with python if this is your first code.Because if we have mutliple modules in our project
#There are some module which we will run first.So let consider sepcial variable_name is first module
#So first module name is always 'main' becuase the point of execution where execution starts.

#So here the value of name is 'main'
#But if go into another file where I write only print("Hello " + __name__).
#If you run this file it will print "Hello __main__" because you running that file.
#But if you import here that file

# import Calc
# print(__name__) #

#So now whatever present in 'Calc' will come to this special file including print statment.
#So If we run this file then this file will print 'main' but what about Cal file it will prin the module name
#It means if we are running Cal it will print 'main' but we are importing Cal in another file then it
#will print name of the module.

#So it menas the value of the 'name' will be chnages as per the place where we are using it
#If we are running the code as main code and using 'name' it will print 'main'
#But if we print 'name' which is imported as module it will print module name.

def add():
    print("From SP adding numbers :")

def main():
    print("Hello")
    print("Welcome User")

if __name__ == "__main__":
    main()


#Why it is helpful
#When we worked on a project everything will be in a function.

#Lets say I want to print two statments when this file is the first file.
#But the problem is when we go to Calc file where we are importing this file and Cal have its own statement.
#And now we are in Cal since it is our first code we are not ruuning this file we are running Cal file
#So this file becomes module for us ,but if we print Cal file it will print statement from this file and Cal file
#I dont want to that so to avoid that we can define print statment of this file in fn.
#I want to call this function only when this is my first code in this we check using above code.
