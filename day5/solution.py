#!/usr/bin/python3

class almanac_map():
    def __init__(self, name, mappings_list):
        self.mappings_list = mappings_list
        self.name = name


    def map(self, key):
        for dest, source, map_range in self.mappings_list:
            if source <= key < source + map_range:
                return key - source + dest
        return key
    
    def __repr__(self):
        return f"<name={self.name},mappings={self.mappings_list}>" 




def main():

    lines = []

    with open("./input", "r") as f:
        for line in f:
            lines.append(line.strip())

    lines = [x for x in lines if x != ""]

    maps = []
    
    for i in range(len(lines)):
        if i == 0:
            seeds = [int(x) for x in lines[i].split(":")[1].strip().split(" ")]
            continue

        if ":" in lines[i]:
            curr_map_name = lines[i].strip()[:-1]
            curr_map_vals = []
        else:
            curr_map_vals.append([int(x) for x in lines[i].strip().split(" ")])
            try:
                if ":" in lines[i+1]:
                    maps.append(almanac_map(curr_map_name, curr_map_vals))
            except IndexError:
                maps.append(almanac_map(curr_map_name, curr_map_vals))
    
    # print(maps)

    seed_locations = []
    seed_mappings = []

    for seed in seeds:
        curr_val = seed
        this_seed_mappings = []
        for m in maps:
            this_seed_mappings.append([m.name, curr_val])
            curr_val = m.map(curr_val)

        seed_locations.append(curr_val)
        seed_mappings.append(this_seed_mappings)

    # print(seed_mappings)
    print(sorted(seed_locations)[0])






if __name__ == "__main__":
    main()