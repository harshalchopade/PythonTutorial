a= 10
b= 20

print("Value of a before swap: ", a)
print("Value of b before swap: ", b)
a= a*b
b=a/b
a=a/b

print("Value of a after swap: ", int(a))
print("Value of b after swap: ", int(b))

#APPROACH2
#a= a^b
#b=a^b
#a=a^b

#APPROACH3
#a= a+b
#b=a-b
#a=a-b

#APPROACH4 - Rotation 2 Approach using here
#a,b = b,a