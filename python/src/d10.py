#!/usr/bin/env python3

from dataclasses import dataclass
from sys import _current_frames

grid:tuple[str, ...] = tuple()

valid_next_moves:dict[str, dict[tuple[int, int], tuple[str, str, str]|tuple]] = {
    "S" : {
        (0, -1): ("|", "7", "F"),   # UP
        (0, 1): ("|", "L", "J"),    # DOWN
        (-1, 0): ("-", "L", "F"),   # LEFT
        (1, 0): ("-", "7", "J")     # RIGHT
    },
    "|" : {
        (0, -1): ("|", "7", "F", "S"),  # UP   
        (0, 1): ("|", "L", "J", "S"),   # DOWN 
        (-1, 0): (),                    # LEFT 
        (1, 0): ()                      # RIGHT
    },
    "-" : {
        (0, -1): (),                    # UP   
        (0, 1): (),                     # DOWN 
        (-1, 0): ("-", "L", "F", "S"),  # LEFT 
        (1, 0): ("-", "7", "J", "S")    # RIGHT
    },
    "7" : {
        (0, -1): (),                    # UP   
        (0, 1): ("|", "L", "J", "S"),   # DOWN 
        (-1, 0): ("-", "L", "F", "S"),  # LEFT 
        (1, 0): ()                      # RIGHT
    },
    "F" : {
        (0, -1): (),                    # UP   
        (0, 1): ("|", "L", "J", "S"),   # DOWN 
        (-1, 0): (),                    # LEFT 
        (1, 0): ("-", "7", "J", "S")    # RIGHT
    },
    "L" : {
        (0, -1): ("|", "7", "F", "S"),  # UP   
        (0, 1): (),                     # DOWN 
        (-1, 0): (),                    # LEFT 
        (1, 0): ("-", "7", "J", "S")    # RIGHT
    },
    "J" : {
        (0, -1): ("|", "7", "F", "S"),  # UP   
        (0, 1): (),                     # DOWN 
        (-1, 0): ("-", "L", "F", "S"),  # LEFT 
        (1, 0): ()                      # RIGHT
    },
}


offset_list:tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]] = ((0, -1), (0, 1), (-1, 0), (1, 0))


@dataclass
class Point:
    x:int = 0
    y:int = 0


@dataclass
class Pointer:
    curr:Point
    prev:Point

    def move_next(self):
        for offset in offset_list:
            if self.check_next(offset):
                self.prev = self.curr
                self.curr = Point(self.prev.x + offset[0], self.prev.y + offset[1])
                break

    def check_next(self, offset:tuple[int, int]) -> bool:
        next:Point = Point(self.curr.x + offset[0], self.curr.y + offset[1])
        if next == self.prev or next.x < 0 or next.x >= 140 or next.y < 0 or next.y >= 140:
            return False

        next_node:str = get_node(next)
        curr_node:str = get_node(self.curr)

        is_valid:bool = next_node in valid_next_moves[curr_node][offset]
        return is_valid

    def __str__(self) -> str:
        return f"x:{self.curr.x} y:{self.curr.y} - node: {grid[self.curr.y][self.curr.x]}"

    def __repr__(self) -> str:
        return f"x:{self.curr.x} y:{self.curr.y} - node: {grid[self.curr.y][self.curr.x]}"


def get_node(point:Point) -> str:
    return grid[point.y][point.x]


def main(file_path:str) -> None:
    global grid
    grid = read_file(file_path)

    steps:int = 1

    start_point:Point = get_start_point()
    a:Pointer = Pointer(Point(start_point.x - 1, start_point.y), start_point)
    b:Pointer = Pointer(Point(start_point.x, start_point.y + 1), start_point)

    while a.curr != b.curr:
        a.move_next()
        b.move_next()
        steps += 1

    print(f"{steps = }")


def main_p2(file_path:str) -> None:
    global grid
    grid = read_file(file_path)

    start_point:Point = get_start_point()
    next_point:Point = Point(start_point.x - 1, start_point.y)

    pointer:Pointer = Pointer(next_point, start_point)

    points:list[Point] = [start_point, next_point]

    while True:
        pointer.move_next()

        if pointer.curr == start_point:
            break
        else:
            points.append(pointer.curr)

    print(f"{len(points) = }")

    # shoelace formula to find area of enclosed polygon
    area:int = 0
    index:int = 0
    while True:
        p1:Point = points[index]
        if index + 1 == len(points):
            p2:Point = points[0]
        else:
            p2:Point = points[index + 1]

        area += (p1.y + p2.y) * (p1.x - p2.x)
        
        index += 1
        if index == len(points):
            break

    area //= 2
    print(f"{area = }")

    # pick's theorem to find number of interior points within an enclosed polygon
    i:int = area - (len(points) // 2) + 1
    print(f"{i = }")
    

def get_start_point() -> Point:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                return Point(x, y)

    raise ValueError(f"Unable to find starting point")


def read_file(file_path:str) -> tuple[str, ...]:
    with open (file_path, 'r') as f:
        lines = f.readlines()
        return tuple(line.strip("\n") for line in lines)


if __name__ == "__main__":
    main_p2("../data/d10.txt")
