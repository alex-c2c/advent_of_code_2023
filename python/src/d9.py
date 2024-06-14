#!/usr/bin/env python3

from os import read
from types import new_class


def main(file_path:str) -> None:
    readings = read_file(file_path)

    next_list:list[int] = []

    for reading in readings:
        next_list.append(reading[0] - process_reading(reading))

    sum:int = 0
    for next in next_list:
        sum += next

    print(f"{sum = }")


def process_reading(reading:tuple[int, ...]) -> int:
    all_zero:bool = True
    for value in reading:
        if value != 0:
            all_zero = False
            break

    if all_zero:
        return 0

    new_list:list[int] = []
    a:int = 0
    b:int = 1
    while b < len(reading):
        new_list.append(reading[b] - reading[a])
        a += 1
        b += 1

    value:int = new_list[0] - process_reading(tuple(new_list))
    return value


def read_file(file_path:str) -> tuple[tuple[int, ...], ...]:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return tuple(process_line(line.strip("\n")) for line in lines)


def process_line(line:str) -> tuple[int, ...]:
    return tuple(int(digit) for digit in line.split(" ") if digit != "")


if __name__ == "__main__":
    main("../data/d9.txt")
