
class Elf:
    def __init__(self, elf_count, calories):
        self.elf_count = elf_count
        self.calories = calories

    def __str__(self):
        return f"This is elf number {self.elf_count} and he has {self.calories} calories\n"
    

def create_elfes():
    elfes = list()
    calories = 0
    elf_count = 0
    with open('input.txt', 'r', encoding='UTF8') as elf_file:
        calories = int(elf_file.readline())
        #print(int(calories))
        for line in elf_file:
            if line.strip(): #not empty line
                calories += int(line.strip())
            else: #empty line
                elfes.append(Elf(elf_count, calories))
                elf_count += 1
                calories = 0   
    return elfes 

def find_most_calories(elf_list: list):
    elf_with_most_cal = elf_list[0]
    for elf in elf_list:
        if elf.calories > elf_with_most_cal.calories:
            elf_with_most_cal = elf
    return elf_with_most_cal

def top_elfes(elf_list: list, elfes: int):
    top_elfes = list()
    for i in range(elfes):
        top_elf = find_most_calories(elf_list)
        top_elfes.append(top_elf)
        elf_list.pop(top_elf.elf_count - i)
    return top_elfes
            
            
if __name__ == "__main__":
    elfes_list = create_elfes()
    elf_most_cal = find_most_calories(elfes_list)
    print(elf_most_cal)
    
    top_elfes = top_elfes(elfes_list, 3)
    
    summ = 0
    for i in top_elfes:
        summ += i.calories
        
    print(summ)

        
