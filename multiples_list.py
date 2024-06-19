import math
factor = int(input())
count = int(input())
my_list =[]
last_number =0
for i in range(count):
    if i==0 :
        my_list.append(factor)
        last_number = factor
    else:
        last_number = last_number+factor
        my_list.append(last_number)

print(my_list)