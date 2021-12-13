def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2, n):
            sum = a + b
            a = b
            b = sum
            print(sum)



fibonacci(10)

#####################################################################3
#Without third var
def alt_fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        a, b = b, a + b
        print(b)

alt_fib(10)
