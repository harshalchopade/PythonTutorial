#Type of arguments
#As we know how to pass the paramaters to the function or we called as arguments
#There are different type of args we can use in different way

def add(a,b):
    c= a+b
    print(c)

add(4,5)

#In the above example when we call add() we have to pass two values we cant simply pass blank
# so when are accepting two args we also need to pass two args.O/w it will give error.

#In above function the 'a' and 'b' are formal arguments and 4 ,5 are actual arguments.
#Actual args has 4 types in itself
#1.position 2.Keyowrd 3.default 4.Variable length

#Position
def person(name,age):
    print(name)
    print(age)

person('harsh', '18')

#In above example when we are calling we are passing name and age.
#But how we know name is going in name and age in age var.
#Position comes into the picture, if we have 10 vars and we want to make sure that the value assigned to a prticular
#var we have to take of vars positions.i.e we need to maintain the seq

#Keyword
#But what if i dont know the seq If I have defined somewhere else where I dont have access to this fn.
#I know function takes 2 args but not sure about sequence, If I forgot the sequence and interchange the position of vars
#Then in that case mentioned keywords i.e var name while passing the values to function
#In below code we use person(name='harsh', age='18')
#To know the function details press ctrl and hover on it.
def person(name,age):
    print(name)
    print(age)

person(name='harsh', age='18')

#Default
#In the below example if I don't want to pass age while calling the function then by default it should take
# some standard value
#If calling we pass the age value it will override exisiting default value.

def person(name,age=18):
    print(name)
    print(age)

person(name='harsh')

#Variable Length
#In the below example we want to add two numbers, but sometimes that may not be the case we need to more than two numbers
#Then how we can pass the multiple values
#As a user am not sure how many values I will pass so to create fn which will accepts multiple args so to do that var length concept came
#It means we can define a function where number of args are not fixed
#So to do that add '*' before variable

def add(a,*b):
    c = a
    for i in b:
        c = c+ i
    print(c)

add(4,5,6,7,8)

#Keyworded Variable Length Arguments
#In variable length we pass the multiple values to the variable but there is one problem
#If I want to work with data lets say we want to print all data here that data will be in tuple so we need to use
#for loop to print it.
#But the problem is if I want to print it individually,and I even dont know what user is sending in data var.
#What is 28 is it phone no or age? WHat is Nagpur is it workplace or native place? so in that case we also need to mention
#keyword along with value to identify the values meant for.
#So if we want to pass multiple data that too with keyword use '**' before var


def person(name, *data):
    print(name)
    print(data)

person('harsh', 28, 'Nagpur',998545)

def person(name, **data):
    print(name)
    print(data)

person('harsh', age=28, place='Nagpur',no=998545)

#To print key -value pair
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('harsh', age=28, place='Nagpur',no=998545)