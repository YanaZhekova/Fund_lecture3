text = input().split("#")
amount_of_water = int(input())

cells_list = []
effort = 0.0
total_fire = 0.0
for i in text:
    f = i.split(" = ")
    cells = int(f[1])
    type_of_fire = f[0]

    if type_of_fire == "High":
        if 81 <= cells <= 125:
            if amount_of_water - cells >= 0:
                amount_of_water -= cells
                effort += cells * 0.25
                total_fire += cells
                cells_list.append(cells)
    elif type_of_fire == "Medium":
        if 51 <= cells <= 80:
            if amount_of_water - cells >= 0:
                amount_of_water -= cells
                effort += cells * 0.25
                total_fire += cells
                cells_list.append(cells)
    elif type_of_fire == "Low":
        if 1 <= cells <= 50:
            if amount_of_water - cells >= 0:
                amount_of_water -= cells
                effort += cells * 0.25
                total_fire += cells
                cells_list.append(cells)

print("Cells:")

for i in cells_list:
    print(" - " + str(i))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire:.0f}")
