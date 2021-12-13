#For Loop
#It works with sequence(list, tuple, string etc) instead of conditions.
#It will be used when we need the o/p on individual basis.

#In below for loop i represents the one element of the list at a time i.one by one it will fetch the values.
#In for loops we dont declare variable, not check the condition and also will not increment/decrement the variable.
#All the above things will be done automatically by the for loop

x= [1,2,"Harshal",3.4]

#print(x) o/p: ['1','2',"Harshal",'3.4']

for i in x:
    print("The element of the list:", i)
#o/p
# 1
# 2
# Harshal
# 3.4

str ='Harshal'
for j in str:
    print(j)

for k in [1,2,3,4]:
    print(k)
#o/p
#1
# 2
# 3
# 4

for l in range(10):
    print(l)
#o/p
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for m in range(11,21,1): #here it will start from 11 and increment by 1 till 21 (value 21 is excluded)
    print(l)

for n in range(21,11,-1): #here it will start from 21 and decrease by 1 till 11 (value 11 is excluded)
    print(l)

for o in range(1,21):
    if (o%5!=0):
        print("The no is :", o)

#Note -  we can use nested for loops also.