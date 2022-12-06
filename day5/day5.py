
def getAllStaks():
    cargo_array = []
    with open('input.txt', 'r', encoding='UTF8') as stacks:
        count_lines = 0
        readInstructions = False
        instructions = []

        for line in stacks:
            letter_row_array = line.strip("\n")
            if readInstructions:

                listen = []
                if letter_row_array == "":
                    continue
                else:
                    new_instruction_array = letter_row_array.split(" ")
                for letter in new_instruction_array:
                    try:
                        listen.append(int(letter))
                    except ValueError:
                        continue
                instructions.append(listen)
            else:
                count = 0
                #print(letter_row_array)
                if count_lines < 1:
                    for i in range((len(letter_row_array) // 4)+1):
                        cargo_array.append({i: []})
                count_lines += 1
                #print(cargo_array)
                for letter in range(1, len(letter_row_array), 4):
                    let = letter_row_array[letter]
                    if let == "1":
                        readInstructions = True
                        break
                    if let == " ":
                        count += 1
                        continue
                    cargo_array[count][count].append(let)
                    count += 1
        return instructions, cargo_array

def moveCrates(allStacks: list, movelist: list):
    for lists in movelist:
        from_move = lists[1]-1
        to_move = lists[2]-1
        for leng in range(lists[0]):
            if len(allStacks[from_move][from_move]) > 0:
                allStacks[to_move][to_move].append(allStacks[from_move][from_move].pop())
    return allStacks


def moveCratesSameOrder(allStacks: list, movelist: list):
    for lists in movelist:
        same_order_move_list = []
        from_move = lists[1]-1
        to_move = lists[2]-1
        for leng in range(lists[0]):
            if len(allStacks[from_move][from_move]) > 0:
                same_order_move_list.append(allStacks[from_move][from_move].pop())
        same_order_move_list.reverse()
        for items in same_order_move_list:
            allStacks[to_move][to_move].append(items)
    return allStacks


if __name__ == '__main__':
    instructions, cargo_array = getAllStaks()
    instructions2, cargo_array2 = getAllStaks()

    for i, dictss in enumerate(cargo_array):
        dictss[i].reverse()

    stack_list = moveCrates(cargo_array, instructions)
    string_answear1 = ""
    for i, let in enumerate(stack_list):
        if len(let[i]) > 0:
            string_answear1 += let[i][-1]
    print(f"Answear1: {string_answear1}")

    for i, dictss in enumerate(cargo_array2):
        dictss[i].reverse()

    print()
    new_stack_list_v2 = moveCratesSameOrder(cargo_array2, instructions2)
    string_answear2 = ""
    for i, let in enumerate(new_stack_list_v2):
        if len(let[i]) > 0:
            string_answear2 += let[i][-1]
    print(f"Answear2:  {string_answear2}")


