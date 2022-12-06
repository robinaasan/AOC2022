
def splitItem(line: str):
    pass

def readItems(): #return object with all list of compartments
    all_items = list()
    with open('input.txt', 'r', encoding='UTF8') as elf_item:
        for line in elf_item:
            line = line.strip()
            mid = len(line) // 2
            compartment1 = line[0:mid]
            compartment2 = line[mid: len(line)]
            all_items.append({"item": [compartment1, compartment2]})
            container = dict()
    return all_items

def getValueLetter(letter: str):
    if letter == letter.upper():
        val = ord(letter) - 38
    else:
        val = ord(letter) - 96
    return val


def findCommonValueCompartment(items: list):
    save_values_letters = 0
    for item in items:
        compartment1 = item["item"][0]
        compartment2 = item["item"][1]
        ignore_list = []
        for letter in compartment1:
            # if go_to_next:
                # go_to_next = False
                # break
            for letter2 in compartment2:
                if (letter == letter2) and (letter not in ignore_list):
                    ignore_list.append(letter)
                    value = getValueLetter(letter)
                    save_values_letters += value

                    # go_to_next = True
                    # break
        #print(compartment1, compartment2)
    return save_values_letters

def findCommonPerThree(items: list):
    with open('input.txt', 'r', encoding='UTF8') as elf_item:
        val = 0
        li = elf_item.readlines()
        for line in range(0, len(li), 3): #every three lines
            save = []
            li[line] = li[line].strip()
            li[line+1] = li[line+1].strip()
            li[line+2] = li[line+2].strip()
            for j in range(len(li[line])):
                if (li[line][j] in li[line+1]) and (li[line][j] in li[line+2]) and li[line][j] not in save:
                    save.append(li[line][j])
                    val += getValueLetter(li[line][j])
        return val




if __name__ == '__main__':
    items = readItems()
    # findCommonValueCompartment(items)
    #vals = findCommonValueCompartment(items)
    # # print(vals)
    #val = getValueLetter("z")
    val = findCommonPerThree(items)
    print(val)
