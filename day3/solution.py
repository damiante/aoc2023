#!/usr/bin/python3


CONTENTS = []


class located_number:
    def __init__(self, str_number, row, start_column):
        self.str_number = str_number
        self.start_column = start_column
        self.row = row

    def number(self):
        return int(self.str_number)

    def str_number(self):
        return self.number

    def __repr__(self):
        return "<val:" + self.str_number + ",row:" + str(self.row) + ",col:" + str(self.start_column) + ">" 



def parse_line(line, row_number):
    numbers = []

    counting_number = False

    curr_number = None

    for i in range(len(line)):
        if not line[i].isdigit() and not counting_number:
            continue
        elif not line[i].isdigit() and counting_number:
            numbers.append(located_number(curr_number, row_number, i - len(curr_number)))
            curr_number = None
            counting_number = False
        
        if line[i].isdigit() and not counting_number:
            curr_number = line[i]
            counting_number = True
        elif line[i].isdigit() and counting_number:
            curr_number += line[i]

    if curr_number != None:
        numbers.append(located_number(curr_number, row_number, i - len(curr_number)))

    return numbers


def adjacent_to_symbol(number):

    if number.str_number == "752":
        prints = True
    else:
        prints = False

    for i in range(number.row - 1, number.row + 2):
        for j in range(number.start_column - 1, number.start_column + len(number.str_number) + 1):
            try:
                test_char = CONTENTS[i][j]

                if prints:
                    print(f"i={i},j={j},test_char={test_char}")

                if not test_char == "." and not test_char.isdigit():
                    return True
            except IndexError:
                continue

    return False




def main():
    global CONTENTS

    with open("./input", "r") as f:
        for line in f:
            CONTENTS.append(line.strip())

    numbers = []

    for i in range(len(CONTENTS)):
        numbers += parse_line(CONTENTS[i], i)


    # print(numbers)


    adjacent_numbers = []

    for number in numbers:
        if adjacent_to_symbol(number):
            adjacent_numbers.append(number)

    print(adjacent_numbers)



    print(sum([x.number() for x in adjacent_numbers]))

    return



if __name__ == "__main__":
    main()