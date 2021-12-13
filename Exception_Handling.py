
a = 10
b = 5

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a no : "))
    print(k)

except ZeroDivisionError as e :
    print("Divison by zero error", e)

except ValueError as e :
    print("Invalid input", e)

except Exception as e :
    print("Something went wrong", e)

finally:
    print("Resouce closed.")