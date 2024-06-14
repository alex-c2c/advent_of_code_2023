#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Data:
    time:int = 0
    dist_to_beat:int = 0


def process_data(data:Data) -> int:
    count:int = 0
    for x in range(data.time+1):
        press_time = x # also equavaent to speed
        left_time = data.time - press_time
        dist:int = left_time * press_time
        if dist > data.dist_to_beat:
            count += 1

    return count


def read_file(file_path:str) -> tuple[Data, ...]:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        time_tuple = tuple(int(digit) for digit in lines[0].split(":")[1].split(" ") if digit != "")
        dist_tuple = tuple(int(digit) for digit in lines[1].split(":")[1].split(" ") if digit != "")

        return tuple(Data(time_tuple[x], dist_tuple[x]) for x in range(4))


def read_file_p2(file_path:str) -> Data:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        time = int("".join([s for s in lines[0].split(":")[1].split(" ") if s != ""]))
        dist = int("".join([s for s in lines[1].split(":")[1].split(" ") if s != ""]))
        return Data(time, dist)


def main(file_path:str) -> None:
    data_tuple:tuple[Data, ...] = read_file(file_path)

    product:int = 1
    for data in data_tuple:
        product *= process_data(data)

    print(f"{product = }")


def main_p2(file_path:str) -> None:
    data = read_file_p2(file_path)

    count:int = process_data(data)

    print(f"{count = }")


if __name__ == "__main__":
    main_p2("../data/d6.txt")
