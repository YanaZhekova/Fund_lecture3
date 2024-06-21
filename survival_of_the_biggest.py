numbers = input().split(" ")
count = int(input())
my_list = []

for i in numbers:
    number = int(i)
    my_list.append(number)

for i in range(count):
    num = min(my_list)
    my_list.remove(num)

for i in range(0, len(my_list)):
    num = str(my_list[i])
    my_list[i] = num


print((", ").join(my_list))
