text = input()
count_shuffles = int(input())
cards = text.split(" ")

for i in range(count_shuffles):
    for card in range(1, len(cards)-1, 1):
        if card + 2 < len(cards) - 1:
            last_card = cards[card]
            new_card = cards[card + 2]
            temp_card = last_card
            last_card = new_card
            new_card = temp_card
            cards[card] = last_card
            cards[card + 2] = new_card

print(cards)