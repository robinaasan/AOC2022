
def getElfesPairs():
    with open('input.txt', 'r', encoding='UTF8') as elf_pairs:
        elfes_pairs = []
        pairs = elf_pairs.readlines()
        for pair in pairs:
            li = pair.strip().split(",")

            elf1 = li[0].split("-")
            elf2 = li[1].split("-")

            elf1_end = int(elf1[1])
            elf1_start = int(elf1[0])
            elf1_list = [i+elf1_start for i in range(elf1_end-elf1_start+1)]

            elf2_end = int(elf2[1])
            elf2_start = int(elf2[0])
            elf2_list = [i+elf2_start for i in range(elf2_end-elf2_start+1)]

            elfes_pairs.append({"elf1": elf1_list, "elf2": elf2_list})
        return elfes_pairs


def check_overlap(elf_pairs: list):
    overlap_count = 0
    for pair in elf_pairs:
        if len(pair["elf1"]) <= len(pair["elf2"]):
            #check if elf1 is in elf2
            if all(elm in pair["elf2"] for elm in pair["elf1"]):
                overlap_count += 1
        else:
            if all(elm in pair["elf1"] for elm in pair["elf2"]):
                overlap_count += 1
    return overlap_count


def check_overlap_again(elf_pairs: list):
    overlap_count = 0
    for pair in elf_pairs:
        if len(pair["elf1"]) <= len(pair["elf2"]):
            #check if elf1 is in elf2
            if any(elm in pair["elf2"] for elm in pair["elf1"]):
                overlap_count += 1
        else:
            if any(elm in pair["elf1"] for elm in pair["elf2"]):
                overlap_count += 1
    return overlap_count


if __name__ == '__main__':
    elfes_pairs = getElfesPairs()

    counts = check_overlap(elfes_pairs)
    print(f"All in one of the list overlaps: {counts}")

    counts_again = check_overlap_again(elfes_pairs)
    print(f"One number in one of the list overlaps: {counts_again}")
