#if can be use when need to make a decisions based on the certain conditions
#At runtime it will based on certain condition/expression
#In python we dont have braces to enclosed the code, here we have indentention (no of white spaces)
#tab = 4 space

#if statment
x= int(input(("Print enter first no: ")))
y= int(input(("Print enter second no: ")))

if (x>y):
    print("1st entered no is greater.")
else:
    print("2nd entered no is greater.")

#we can have if inside if (nested if statment)
#else statment

if (x>y):
    print("1st entered no is greater.")
    if True:
        print("Entere in nested if block")
else:
    print("2nd entered no is greater.")

#elif statment

no = input("Please enter a no: ")
if(no==1):
    print("One")

elif(no==2):
    print("Two")

elif(no==3):
    print("Three")

elif(no==4):
    print("Four")

else:
    print("Invalid no entered.")