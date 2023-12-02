#!/usr/bin/python3

DIGITS = {
    "one": 1, 
    "two": 2,
    "three": 3, 
    "four": 4,
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9, 
    "zero": 0
    }

def find_digit(s):

    substr = ""

    for char in s:
        if char.isdigit():
            return char
        
        substr += char

        for d in DIGITS.keys():
            if d in substr:
                return str(DIGITS[d])
            elif d[::-1] in substr:
                return str(DIGITS[d])
    
    return None

def score_line(line):
    first_digit = find_digit(line)
    last_digit = find_digit(reversed(line))
    

    if first_digit == None and last_digit == None:
        return 0
    else:
        return int(first_digit + last_digit)


def main():

    count = 0

    with open("./input", "r") as f:
        for line in f:
            count += score_line(line)

    print(count)

    return


if __name__ == "__main__":
    main()