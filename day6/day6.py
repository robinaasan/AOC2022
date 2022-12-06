
def read_input(unlike_chars: int):
    with open('input.txt', 'r', encoding='UTF8') as data_stream:
        for line in data_stream:
            line = line.strip()
            #temp_line_stream = [ch for ch in line[0:4]]
            count = 0
            temp_line_stream = []
            while True:
                while len(temp_line_stream) < unlike_chars: #not in
                    char = line[count]
                    if char not in temp_line_stream:
                        temp_line_stream.append(char)
                        count += 1
                    else:
                        temp_count = len(temp_line_stream)
                        temp_line_stream = temp_line_stream[1:temp_count]
                        break
                else:
                    print(temp_line_stream)
                    print(f"last character is: {line[count-1]}")
                    return count


if __name__ == '__main__':
    count1 = read_input(4)
    print(f"Answear 1 is:{count1}")
    count2 = read_input(14)
    print(f"Answear 2 is:{count2}")

