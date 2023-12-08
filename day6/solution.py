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

    times, distance_records = [], []

    with open("./input", "r") as f:
        first = True
        for line in f:
            if first:
                first = False
                times = [int(x) for x in line.split(":")[1].strip().split(" ") if x]
            else:
                distance_records = [int(x) for x in line.split(":")[1].strip().split(" ") if x]
    
    races = zip(times, distance_records)

    ways_to_beat_races = [ways_to_beat(time, distance) for time, distance in races]

    print(ways_to_beat_races)

    print(prod(ways_to_beat_races))

    return
    



if __name__ == "__main__":
    main()