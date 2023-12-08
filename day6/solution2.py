#!/usr/bin/python3

from numpy import prod


def ways_to_beat(time, distance_record):
    winning_plays_count = 0

    for i in range(time + 1):
        attempt_distance = i * (time - i)
        if attempt_distance > distance_record:
            winning_plays_count += 1

    return winning_plays_count


def main():

    with open("./input", "r") as f:
        first = True
        for line in f:
            if first:
                first = False
                time = ""
                for char in line:
                    time += char if char.isdigit() else ""
                time = int(time)
            else:
                distance_record = ""
                for char in line:
                    distance_record += char if char.isdigit() else ""
                distance_record = int(distance_record)
    
    print(ways_to_beat(time, distance_record))

    return
    



if __name__ == "__main__":
    main()