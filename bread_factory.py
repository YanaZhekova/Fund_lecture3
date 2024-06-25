events = input().split("|")
energy = 100
coins = 100
make_all_events = True
for i in events:
    collect = i.split("-")
    event = collect[0]
    number = int(collect[1])

    if event == "rest":
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {100 - energy} energy.")
            print(f"Current energy: {100}.")

    elif event == "order":
        if energy - 30 > 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            make_all_events = False
    else:
        if coins - number >= 0:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            make_all_events = False
            break

if make_all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
