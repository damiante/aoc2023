#!/usr/bin/python3


from numpy import prod

PARAMS = {
    "red"  : 12,
    "green": 13,
    "blue" : 14
}


def parse_set(set_str):
    set_lst = set_str.split(",")

    set_lst = [x.strip() for x in set_lst]

    result_dict = dict()

    for s in set_lst:
        count, colour = s.split(" ")
        result_dict[colour] = int(count)

    return result_dict


def parse_line(line):

    # ugly list indexing :)
    line = line.strip()
    sep_id = line.split(":")

    id = sep_id[0].split(" ")[1]

    sets_str = sep_id[1]

    unparsed_sets = sets_str.split(";")

    parsed_sets = []

    for s in unparsed_sets:
        parsed_sets.append(parse_set(s))

    return [id, parsed_sets]


def is_valid_game(sets, params):
    
    for s in sets:
        for colour in s.keys():
            if s[colour] > PARAMS[colour]:
                return False

    return True


def minimum_colours(sets):

    minimum_colour_dict = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for s in sets:
        for colour in s:
            if s[colour] > minimum_colour_dict[colour]:
                minimum_colour_dict[colour] = s[colour]
    
    return minimum_colour_dict



def main():

    game_powers = []

    with open("./input", "r") as f:
        for line in f:
            id, sets = parse_line(line)

            # print(f"id is: {id}, sets are: {sets}")

            min_game_colours = minimum_colours(sets)

            power = prod([x for x in min_game_colours.values()])


            game_powers.append(power)


    
    print(sum([int(x) for x in game_powers]))

    return





if __name__ == "__main__":
    main()