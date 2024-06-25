items = input().split("|")
budget = float(input())
bought_items = []
train_ticket = 150
total_price_items = 0.0
for i in items:
    collect = i.split("->")
    item = collect[0]
    price = float(collect[1])
    condition = False
    if price <= budget:
        if item == "Clothes":
            if price <= 50:
                condition = True
        elif item == "Shoes":
            if price <= 35:
                condition = True
        elif item == "Accessories":
            if price <= 20.50:
                condition = True

    if condition:
        if budget >= price:
            budget -= price
            bought_items.append(price)
            total_price_items += price

result = []
sum = 0.0
for i in bought_items:
    i = i + i * 0.4
    i = round(i, 2)
    sum += i
    result.append(f"{i:.2f}")

budget += sum
print(" ".join(result))
profit = sum - total_price_items
if len(bought_items) > 0:
    print(f"Profit: {profit:.2f}")

if budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
