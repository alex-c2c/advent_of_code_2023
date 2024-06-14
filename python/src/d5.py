#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Data:
    line_num:int = 0
    source:int = 0
    dest:int = 0
    range:int = 0


seeds:list[int] = []
seed_to_soil:tuple[Data, ...]
soil_to_fertilizer:tuple[Data, ...]
fertilizer_to_water:tuple[Data, ...]
water_to_light:tuple[Data, ...]
light_to_temp:tuple[Data, ...]
temp_to_humitidy:tuple[Data, ...]
humidity_to_location:tuple[Data, ...]


def main(file_path:str) -> None:
    read_file(file_path)

    lowest_loc:int = 0

    for seed in seeds:
        location = get_loc(seed)

        if lowest_loc == 0:
            lowest_loc = location
        elif location < lowest_loc:
            lowest_loc = location

    print(f"{lowest_loc = }")


def main_p2(file_path:str) -> None:
    read_file(file_path)

    seed_dict:dict[int, int] = {}
    for i in range(len(seeds)):
        if i % 2 == 0:
            seed_dict[seeds[i]] = seeds[i+1]

    htl = list(humidity_to_location)
    htl.sort(key = lambda data: data.dest)

    highest_loc:int = htl[-1].dest + htl[-1].range
    loc1:int = 0
    for x in range(0, highest_loc, 1000):
        seed = get_seed(x)
        if is_seed_valid(seed, seed_dict):
            loc1 = x
            print(f"loc: {x}")
            break

    for x in range(loc1-1000, loc1):
        seed = get_seed(x)
        if is_seed_valid(seed, seed_dict):
            print(f"lowest loc: {x}")
            return


def is_seed_valid(seed:int, seed_dict:dict[int, int]) -> bool:
    for key in seed_dict:
        if seed >= key and seed < key + seed_dict[key]:
            return True

    return False


def get_loc(seed:int) -> int:
    ln, soil = get_dest(seed, seed_to_soil)
    ln, fertilizer = get_dest(soil, soil_to_fertilizer)
    ln, water = get_dest(fertilizer, fertilizer_to_water)
    ln, light = get_dest(water, water_to_light)
    ln, temp = get_dest(light, light_to_temp)
    ln, humidity = get_dest(temp, temp_to_humitidy)
    ln,location = get_dest(humidity, humidity_to_location)

    return location


def get_seed(loc:int) -> int:
    ln, humidity = get_source(loc, humidity_to_location)
    ln, temp = get_source(humidity, temp_to_humitidy)
    ln, light = get_source(temp, light_to_temp)
    ln, water = get_source(light, water_to_light)
    ln, fertilizer = get_source(water, fertilizer_to_water)
    ln, soil = get_source(fertilizer, soil_to_fertilizer)
    ln, seed = get_source(soil, seed_to_soil)

    return seed


def get_lowest_loc() -> tuple[int,int]:
    lowest_loc:int = 0
    lowest_loc_range = 0
    for data in humidity_to_location:
        if lowest_loc == 0:
            lowest_loc = data.dest
            lowest_loc_range = data.range
        elif data.dest < lowest_loc:
            lowest_loc = data.dest
            lowest_loc_range = data.range

    return lowest_loc, lowest_loc_range


def get_source(value:int, data_tuple:tuple[Data, ...]) -> tuple[int, int]:
    for data in data_tuple:
        if value >= data.dest and value < data.dest + data.range:
            diff:int = value - data.dest
            return data.line_num, data.source + diff

    return -1, value


def get_dest(value:int, data_tuple:tuple[Data, ...]) -> tuple[int, int]:
    for data in data_tuple:
        if value >= data.source and value < data.source + data.range:
            diff:int = value - data.source
            return data.line_num, data.dest + diff

    return -1, value


def read_file(file_path:str) -> None:
    global seeds
    global seed_to_soil
    global soil_to_fertilizer
    global fertilizer_to_water
    global water_to_light
    global light_to_temp
    global temp_to_humitidy
    global humidity_to_location

    with open(file_path, 'r') as f:
        lines = f.readlines()

        seed_line = lines[0][6:]
        seeds = [int(seed) for seed in seed_line.split(" ") if seed != ""]

        seed_to_soil = tuple(process_line(x, lines[x]) for x in range(3, 15))
        soil_to_fertilizer = tuple(process_line(x, lines[x]) for x in range(17, 38))
        fertilizer_to_water = tuple(process_line(x, lines[x]) for x in range(40, 56))
        water_to_light = tuple(process_line(x, lines[x]) for x in range(58, 103))
        light_to_temp = tuple(process_line(x, lines[x]) for x in range(105, 152))
        temp_to_humitidy = tuple(process_line(x, lines[x]) for x in range(154, 177))
        humidity_to_location = tuple(process_line(x, lines[x]) for x in range(179, 205))


def process_line(line_num:int, line:str) -> Data:
    values:tuple[int, ...] = tuple(int(digit) for digit in line.strip("\n").split(" ") if digit != "")
    return Data(line_num + 1, values[1], values[0], values[2])


if __name__ == "__main__":
    main_p2("../data/d5.txt")
