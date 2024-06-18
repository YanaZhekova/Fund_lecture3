n = int(input())
my_list = []
result=[]
for i in range(1, n + 1):
    number = int(input())
    my_list.append(number)

command =input()

for i in my_list:

    if command == "even":
        if i % 2 == 0:
            result.append(i)
    elif command == "odd":
        if i % 2 != 0:
            result.append(i)
    elif command == "negative":
        if i < 0:
            result.append(i)
    elif command == "positive":
        if i >= 0:
            result.append(i)
print(result)