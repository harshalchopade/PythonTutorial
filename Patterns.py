for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()


#o/p
# # # #
# # # #
# # # #
# # # #

for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()

#o/p
#
# #
# # #
# # # #

for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()

#o/p
# # # #
# # # #
# # #
# #
#

for i in range(4):
    for j in range(i):
        print("i ", end="")
    print()

for i in range(1,5):
      for j in range(i,5):
            print(j,end=" ")
      print()

#o/p
#1 2 3 4
#2 3 4
#3 4
#4

x='ABCD'
y='PQR'
for i in range(4):
      print(x[:i+1]+y[i:])

#o/p
#APQR
#ABQR
#ABCR
#ABCD