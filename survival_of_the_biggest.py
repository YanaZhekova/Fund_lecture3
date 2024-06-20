text = input().split(" ")
count = int(input())
numbers = []
for i in text:
    current_number = int(i)
    numbers.append(current_number)

numbers.sort()
for i in range(count):
    numbers.remove(numbers[0])
numbers.reverse()
print(numbers)
