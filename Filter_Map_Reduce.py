#filter()
#1.It will accept function as 1st parameter and sequence as second paramters (list, tuple etc)

lst = [2,4,5,8,10,1,3,4]
evens = list(filter(lambda a:a%2==0,lst))
print(evens)

#map()
#It will be used when we filter out some values based on some conditions and want to peroform some operation
# want to perform common operation on all the values.

doubles = list(map(lambda n:n*2, evens))
print(doubles)

#reduce()
#If I want a single value after performing certain operation then go for reduce
#To use this we need to import functools

from functools import reduce

sum = reduce(lambda a,b:a+b, doubles)
print(sum)

#map: Takes a function f, and a list L1, and returns a list L2 obtained by applying f to every element of L1.
# Say f is a function that takes x and returns 2x. Then, map(f, [1,2,3,4]) returns [2,4,6,8].

#reduce: Takes a binary operator f, a list L and a seed value (or identity element).
# It returns the seed value if the list is empty. Otherwise, it applies the binary operator f to the seed
# and first element of L, then applies f to the result of this and the 2nd element of L, and so on till L
# is exhausted. The result is returned. This can be seen as a generalization of factorial function.

#filter: Takes a boolean function f and a list L1.
# It applies the function to each element of L1, and list of those elements that give true is returned.