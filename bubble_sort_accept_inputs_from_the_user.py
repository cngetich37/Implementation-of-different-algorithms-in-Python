# begin with an empty list
my_list = []
# entered numbers are the number of integers that should be entered
entered_numbers = int(input("Please the number of integers:"))

# add other numbers that you were to sort with the entered number
print("enter the values:")
# Iterate through the entered integers as you add to the list
for k in range(entered_numbers):
    my_list.append(int(input()))

# Bubble sort algorithm
for j in range(len(my_list)-1, 0, -1):
    for i in range(j):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print("Sorted list:"+str(my_list))
