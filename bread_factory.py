events = input().split("|")
energy = 100
coins = 100
make_all_events = True
for i in events:
    collect = i.split("-")
    command = collect[0]
    number = int(collect[1])

    if command == "rest":
        if energy + number >= 100:
            print(f"You gained {100-energy} energy.")
            energy = 100
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            # make_all_events = False
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            make_all_events = False
            break

if make_all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
