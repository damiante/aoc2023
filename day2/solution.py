#!/usr/bin/python3


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




def main():

    valid_games = []

    with open("./input", "r") as f:
        for line in f:
            id, sets = parse_line(line)

            # print(f"id is: {id}, sets are: {sets}")


            if is_valid_game(sets, PARAMS):
                valid_games.append(id)


    
    print(sum([int(x) for x in valid_games]))

    return





if __name__ == "__main__":
    main()