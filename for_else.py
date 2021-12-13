#for-else loop
#in the below eg the for loop gets executed fully without even break, so due to that if we dont write else
#it wont print anything on the console.
#But we write else for 'for' then it will be executed only when for loops comes without even breaking on the condition


nums = [10,23,46,32,22]

for num in nums:
    if num%5 == 0:
        print(num)
        break
else:
    print("not found")