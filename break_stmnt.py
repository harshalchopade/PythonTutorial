#break statment is used to break the flow of execution based on the condition
#once break statment encountered it will come out of the loop.
#If there are multiple loop it will come out of inner loop, then next inner loop so on
av = 10
x = int(input("Enter the no of candies you want: "))
i = 1
while i<=x:
    if i>av:
        print("Out of stock.")
        break

    print("Candy")
    i+=1

print("Bye")
