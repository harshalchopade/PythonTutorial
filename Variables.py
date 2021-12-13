#If we use only input() it will always return data in string
a = int(input("Enter 1st No :"))
b = int(input("Enter 2nd No :"))
c = a+b
print("The sum of two nos are :", c)


#To have the control to print the character
ch = input("Please enter a character :")
#if we enter the string here it will take the whole string as i/p.
#But to control that we can use indexing
print(ch[0])

#Or to control while fetching the input only first character
ch = input("Please enter a character :") [0]

#Also we can evaluate the function using eval()
eva = eval(input("Enter the expression:"))
print(eva)

#To pass the argument for command line prompt we need to import sys module first
#Use argv[] pass the index no from 1 as 0 stand for file name in cmd
#Convert it into int or resp data type
import sys
x = sys.argv[1]
y = sys.rgv[2]
z= x+y