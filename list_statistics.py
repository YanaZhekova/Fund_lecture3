n = int(input())
negative_numbers = []
positive_numbers = []
for i in range(1, n + 1):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(positive_numbers)
print(negative_numbers)
sum_negative_numbers = sum(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum_negative_numbers}")
