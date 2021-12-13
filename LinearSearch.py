#In Linear search it is not necessary values to be sorted.
pos = -1

def search(list, n):
    i = 0

    while(i < len(list)):
        if(list[i] == n):
            globals()['pos'] = i
            return True
        i = i+1

    return False

list = [4,7,6,1,7,2,4,5,5]
n = 8

if (search(list, n)):
    print("Found at :", pos+1)

else:
    print("Not Found.")