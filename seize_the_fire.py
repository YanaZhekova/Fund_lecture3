text = input().split("#")
amount_of_water = int(input())

cells_list = []
effort = 0.0
for i in text:
    f = i.split(" = ")
    cells = int(f[0])
    type_of_fire = f[1]
    cells_list.append(cells)
    if type_of_fire == "High":
        if 81 <= cells <= 125:
            amount_of_water -= cells
            effort += cells*0.25
    elif type_of_fire == "Medium":
        if 51 <= cells <= 80:
            amount_of_water -= cells
            effort += cells*0.25
    elif type_of_fire == "Low":
        if 1 <= cells <= 50:
            amount_of_water -= cells
            effort += cells*0.25

cells_list.append(text[len(text) - 1])
print(cells_list)
