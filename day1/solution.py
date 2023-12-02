#!/usr/bin/python3


def score_line(line):
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break

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