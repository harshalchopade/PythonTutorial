#continue statment is use when we need to skip the statment based on condition mentioned
# and want to continue the loop execution normally.


for i in range(1,101):
    if (i%3 ==0 or (i%5 ==0)):
        continue
    print("The no divisible by 3 are : ", i)
print("Bye")