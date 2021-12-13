#If we want to save the data for longer period of time then either we can go for DB or file
#Playing with DB is bit complex as it having data in the form of tables etc
#But in file data can be text etc so easy to work

#Use below syntax to read, write, append and copy the file


file1 = open('MyData', 'r') #to open the file in read mode
print(file1.read())  #to print all the data present in a file
print(file1.readline())

#To write something in the file
file2 = open('MyFile', 'w')  #it will create the file automatically
#print(file2.write("Hello Buddy!!")) #the data provided are written into the file.
#print(file2.write("Hello!")) #if you use again then it will overrride the data
print(file2.write('Data'))

#To append the data into the file
file2 = open('MyFile', 'a')
print(file2.write('Append'))
print(file2.write('Data'))

#To copy the data from file1 to file2
for data in file1:
    file2.write(data)

#Also when you work with img its binary format to mention that use below syntax
#file1 = open('MyData', 'rb')