#we have iterator but we are having some issue with iterator
#we need to have those two fn iter and next
#But we want python to do that for us.
#Generators is like if we want to fetch 1000 of records but you dont want to store those in a memory
#you want to work each record at a time


class TopTen:

    def square(self):
        n = 1
        while n<10:
            sq = n * n
            yield sq
            n += 1

values = TopTen()

for i in values.square():
    print(i)