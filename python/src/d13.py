#!/usr/bin/env python3


from dataclasses import field, dataclass
from os import remove


@dataclass
class Map:
    grid:list[str] = field(default_factory=list)


maps:list[Map] = []


def rotate_grid(grid:list[str]) -> list[str]:
    col_size:int = len(grid[0])

    new_grid:list[str] = []
    for col in range(col_size):
        new_str:str = ""
        for row in range(len(grid)):
            new_str = new_str + grid[row][col]

        new_grid.append(new_str)

    return new_grid


def remove_smudge(grid:list[str]) -> tuple[int, list[str] | None]:
    s:int = 1
    is_removed:bool = False
    new_grid:list[str] = [line for line in grid]

    while s < len(new_grid):
        a:int = s - 1
        b:int = s
        potential_smudge:int = 0
        is_matched:bool = False

        while a >= 0 and b < len(grid):
            diff_count:int = compare_lines(new_grid[a], new_grid[b])
            if is_matched:
                if potential_smudge != 0 and diff_count != 0:
                    is_matched = False
                    break
                elif diff_count == 1:
                    potential_smudge = s
            elif diff_count == 0:
                is_matched = True
            elif diff_count == 1 and b == s:
                potential_smudge = s
                is_matched = True
            else:
                break

            a -= 1
            b += 1

        if is_matched and potential_smudge != 0:
            return (potential_smudge, new_grid)

        s += 1

    return (0, None)


def compare_lines(a:str, b:str) -> int:
    diff_count:int = 0
    for index in range(len(a)):
        if a[index] != b[index]:
            diff_count += 1

    return diff_count


# find the horizontal relection index
def find_reflect(grid:list[str]) -> int:
    s:int = 1
    is_match:bool = False

    while s < len(grid):
        a:int = s - 1
        b:int = s
        is_match:bool = False

        while a >= 0 and b < len(grid):
            if grid[a] == grid[b]:
                is_match = True
            else:
                is_match = False
                break

            a -= 1
            b += 1

        if is_match:
            return s

        s += 1

    return 0


def main(file_path:str) -> None:
    read_file(file_path)

    sum:int = 0
    h_smudge:int = 0
    v_smudge:int = 0

    index:int = 0
    for map in maps:
        hr:int = 0
        vr:int = 0

        hr, new_grid = remove_smudge(map.grid)
        if new_grid is not None:
            #hr = find_reflect(new_grid)
            h_smudge += 1
            print(f"{index = } horizontal smudge: {hr = }")
        else:
            vr, new_grid = remove_smudge(rotate_grid(map.grid))
            if new_grid is not None:
                #vr = find_reflect(rotate_grid(new_grid))
                v_smudge += 1
                print(f"{index = } vertical smudge {vr = }")

        sum += vr
        sum += hr * 100
        index += 1

    print(f"{h_smudge = } - {v_smudge = }")
    print(f"{sum = }")


def read_file(file_path:str) -> None:
    global maps

    with open (file_path, 'r') as f:
        lines:list[str] = [line.strip("\n") for line in f.readlines()]

        index:int = 0
        while True:
            new_map = Map([])
            while lines[index] != "":
                new_map.grid.append(lines[index])
                index += 1

            if lines[index] == "":
                maps.append(new_map)
                index += 1

            if index >= len(lines):
                break

    print(f"{len(maps)}")


if __name__ == "__main__":
    main("../data/d13.txt")
