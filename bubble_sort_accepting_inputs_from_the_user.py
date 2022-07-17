#begin with an empty list
my_list = []
#Ask users to enter the numbers
entered_numbers = int(input("Please enter the number:"))

#add other numbers that you were to sort with the entered number
print("add other numbers")
#Iterate through the entered integers as you add to the list
for k in range(entered_numbers):
    my_list.append(int(input()))

for j in range(len(my_list)-1,0,-1):
    for i in range(j):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print("Sorted list:"+str(my_list))



