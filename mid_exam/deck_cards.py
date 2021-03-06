def add(my_list, card):
    if card in my_list:
        print("Card is already bought")
    else:
        my_list.append(card)
        print("Card successfully bought")
    return my_list


def remove(my_list, card):
    if card in my_list:
        print("Card successfully sold")
        my_list.remove(card)
    else:
        print("Card not found")
    return my_list


def remove_at(my_list, i):
    if 0 <= i < len(my_list):
        my_list.pop(i)
        print("Card successfully sold")
    else:
        print("Index out of range")
    return my_list


def insert(my_list, i, card):
    if 0 <= i < len(my_list):
        if card in my_list:
            print("Card is already bought")
        else:
            print("Card successfully bought")
            my_list.insert(i, card)
    else:
        print("Index out of range")
    return my_list


owned_cards = input().split(", ")
n_commands = int(input())

for _ in range(n_commands):
    command = input().split(", ")
    action = command[0]

    if action == "Add":
        card = command[1]
        owned_cards = add(owned_cards, card)
    elif action == "Remove":
        card = command[1]
        owned_cards = remove(owned_cards, card)
    elif action == "Remove At":
        index = int(command[1])
        owned_cards = remove_at(owned_cards, index)
    elif action == "Insert":
        index = int(command[1])
        card = command[2]
        owned_cards = insert(owned_cards, index, card)

print(", ".join(owned_cards))
