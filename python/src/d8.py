#!/usr/bin/env python3

from dataclasses import dataclass
from math import lcm

@dataclass
class Nav:
    left:str = ""
    right:str = ""


ii:int = -1
instructions:str = ""
mappings:dict[str, Nav] = {}


def main(file_path:str) -> None:
    read_file(file_path)

    step:int = 0
    current_node:str = "AAA"
    while current_node != "ZZZ":
        if next_dir(step) == "L":
            current_node = mappings[current_node].left
        else:
            current_node = mappings[current_node].right

        step += 1

    print(f"{step = }")


def main_p2(file_path:str) -> None:
    read_file(file_path)

    step_list:list[int] = []
    starting_nodes = tuple(key for key in mappings if key[2] == "A")
    print(f"starting nodes: {starting_nodes}")

    for node in starting_nodes:
        start = node
        step:int = 0
        while node[2] != "Z":
            if next_dir(step) == "L":
                node = mappings[node].left
            else:
                node = mappings[node].right

            step += 1   

        print(f"{start} -> {node} in {step} steps")

        step_list.append(step)

    print(f"{lcm(*step_list) = }")


def next_dir(index:int) -> str:
    if index >= len(instructions):
        index = index % len(instructions)

    return instructions[index]


def read_file(file_path:str) -> None:
    with open(file_path, 'r') as f:
        lines = f.readlines()

        global mapping
        global instructions
        instructions = lines[0].strip("\n")

        for line in lines[2:]:
            new_line:str = line.strip("\n").replace("(", "").replace(")", "")
            line_split:list[str] = new_line.split(" = ")
            nav_split:list[str] = line_split[1].split(", ")

            mappings[line_split[0]] = Nav(nav_split[0], nav_split[1])


if __name__ == "__main__":
    main_p2("../data/d8.txt")
