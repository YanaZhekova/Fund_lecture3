n = int(input())
text = input()
my_list = []
result=[]
for i in range(1,n+1):
    current_text = input()
    my_list.append(current_text)

for i in my_list:
    if i.__contains__(text):
        result.append(i)
print(my_list)
print(result)