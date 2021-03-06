def contains(string_list, substring):
    if substring in string_list:
        print(f"{string_list} contains {substring}")
    else:
        print(f"Substring not found!")


def flip(string_list, case, start, end):
    if case == "Upper":
        string_list = string_list.replace(string_list[start:end], string_list[start:end].upper())
    else:
        string_list = string_list.replace(string_list[start:end], string_list[start:end].lower())

    return string_list


def sliced(string_list, start, end):
    string_list = string_list.replace(string_list[start:end], "")

    return string_list


activation_key = input()

command = input()


while not command == "Generate":
    command.split(">>>")
    action = command.split(">>>")[0]

    if action == "Contains":
        substring = command.split(">>>")[1]
        contains(activation_key, substring)

    elif action == "Flip":
        letter_case = command.split(">>>")[1]
        start_index = int(command.split(">>>")[2])
        end_index = int(command.split(">>>")[3])
        activation_key = flip(activation_key, letter_case, start_index, end_index)
        print(activation_key)

    elif action == "Slice":
        start_i = int(command.split(">>>")[1])
        end_i = int(command.split(">>>")[2])
        activation_key = sliced(activation_key, start_i, end_i)
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")