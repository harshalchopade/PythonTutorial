
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+= 1
        else:
            odd+=1

    return even, odd

lst = [10,12,14,16,13,15,17,19,21]
even, odd = count(lst)
print("Even : {} and Odd: {}".format(even, odd))

###########################################################################3
lst=[]
for i in range(5):
    x = input("Enter the name")
    lst.append(x)
def count(lst):
    greater = 0
    lesser = 0
    for i in lst:
        if len(i) >= 5:
            greater += 1
        else:
            lesser += 1
    return greater,lesser
greater,lesser = count(lst)
print("greater : {} and lesser : {}".format(greater,lesser))
