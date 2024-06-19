import math
text = input()

my_list = text.split(" ")

for i in range(len(my_list)):
    number = int(my_list[i])
    if number > 0:
        number = -number
    elif number < 0:
        number =my_list[i].split("-")
        number = number[1]
    my_list[i] = int(number)

print(my_list)