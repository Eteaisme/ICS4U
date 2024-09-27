my_list = [9, 2, 4 ,5, 1, -2, 4]
my_list.append(10)

running_total = 0
for i in range(len(my_list)):
    running_total = running_total + my_list[i]

print("The sum of this list is: ", running_total)
