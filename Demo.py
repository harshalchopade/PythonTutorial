def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("Value of x is: ", x)

a = 20
print(id(a))
update(a)
print("Value of x is: ", a)