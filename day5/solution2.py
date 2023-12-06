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

    def reverse_map(self, val):
        for dest, source, map_range in self.mappings_list:
            if dest <= val < dest + map_range:
                return val - dest + source
        return val
            
    
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
            seed_input = [int(x) for x in lines[i].split(":")[1].strip().split(" ")]
            seed_pairs = [(seed_input[i],seed_input[i+1]) for i in range(0,len(seed_input),2)]
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
    


    # instead, try going up in all possible locations and map backwards to find a seed

    location = 0
    while True:
        curr_val = location
        for m in reversed(maps):
            curr_val = m.reverse_map(curr_val)
        
        
        for seed_pair in seed_pairs:
            if seed_pair[0] <= curr_val < seed_pair[0] + seed_pair[1]:
                print(location)
                exit(0)

        if location % 100000 == 0:
            print(f"Up to {location}")

        location += 1

        if location > 999999999999999:
            print(":(")
            exit(1)






if __name__ == "__main__":
    main()