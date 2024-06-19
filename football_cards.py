text = input()
cards = text.split(" ")
teamA = 11
teamB = 11
list_double_cards_A = []
list_double_cards_B = []
terminated_game = False

for card in cards:
    team = card[0]
    number_of_player = card.split("-")[1]

    if team == "A":
        if not list_double_cards_A.__contains__(number_of_player):
            teamA -= 1
            list_double_cards_A.append(number_of_player)

    elif team == "B":
        if not list_double_cards_B.__contains__(number_of_player):
            teamB -= 1
            list_double_cards_B.append(number_of_player)

    if teamA < 7 or teamB < 7:
        terminated_game = True
        break

print(f"Team A - {teamA}; Team B - {teamB}")
if terminated_game:
    print("Game was terminated")
