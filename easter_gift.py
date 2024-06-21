gifts = input().split(" ")
commands = input()
result = []
while commands != "No Money":
    command = commands.split(" ")
    com = command[0]
    if 2 >= len(command) > 1:
        gift = commands.split(" ")[1]
    else:
        gift = commands.split(" ")[1]
        index = int(commands.split(" ")[2])
    if com == "OutOfStock":
        if gifts.__contains__(gift):
            for i in range(0, len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = "None"

    elif com == "Required":
        if 0 < index < len(gifts):
            gifts[index] = gift
    elif com == "JustInCase":
        gifts[len(gifts) - 1] = gift
    commands = input()

for gift in gifts:
    if gift != "None":
        result.append(gift)

print(" ".join(result))
