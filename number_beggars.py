text = input()
count_beggars = int(input())

numbers = text.split(", ")

new_list = []
last_number = 0
for i in (0, len(numbers), +count_beggars):
    current_number = int(numbers[i])
    new_list.append(current_number + last_number)
    last_number = current_number

    if i + count_beggars > len(numbers):
        current_number = 0
        new_list.append(current_number + last_number)

print(new_list)
