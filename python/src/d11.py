#!usr/bin/env python3

space:list[list[str]] = []
empty_row:list[int] = []
empty_col:list[int] = []

def main(file_path:str) -> None:
    read_file(file_path)

    find_empty_area()

    #expand_space()

    galaxys:list[tuple[int, int]] = []

    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] == "#":
                galaxys.append((x, y))

    dist_dict:dict[tuple[tuple[int, int], tuple[int, int]], int] = {}

    for i in range(len(galaxys)):
        a:tuple[int, int] = galaxys[i]

        for j in range(len(galaxys)):
            if i == j:
                continue

            b:tuple[int, int] = galaxys[j]
            if dist_dict.get((a, b), None) is None and dist_dict.get((b, a), None) is None:
                dist_dict[(a, b)] = get_dist(a, b)

    sum:int = 0
    for key in dist_dict:
        sum += dist_dict[key]

    print(f"{sum = }")

    #test = get_dist(galaxys[0], galaxys[7])

def get_dist(a:tuple[int, int], b:tuple[int, int]) -> int:
    compensate_x:int = 0
    compensate_y:int = 0

    for index in empty_col:
        if a[0] < index and b[0] > index or b[0] < index and a[0] > index:
            compensate_x += 999999

    for index in empty_row:
        if a[1] < index and b[1] > index or b[1] < index and a[1] > index:
            compensate_y += 999999

    dist = abs(b[0] - a[0]) + compensate_x + abs(b[1] - a[1]) + compensate_y
    #print(f"{a = } | {b = } | {dist = }")
    return dist


def find_empty_area() -> None:
    global empty_row
    global empty_col

    for x in range(len(space)):
        if is_row_empty(x):
            empty_row.append(x)

    for x in range(len(space[0])):
        if is_col_empty(x):
            empty_col.append(x)

    print(f"{empty_row = }")
    print(f"{empty_col = }")


def expand_space() -> None:
    global space
    global empty_row
    global empty_col

    empty_row.sort(reverse=True)
    empty_col.sort(reverse=True)

    col_size:int = len(space[0])
    for index in empty_row:
        space.insert(index, ["." for _ in range(col_size)])

    for index in empty_col:
        for row in space:
            row.insert(index, ".")


def is_row_empty(index:int) -> bool:
    if index < 0 or index >= len(space):
        raise IndexError(f"{index} is out of space bounds")

    return "#" not in space[index]


def is_col_empty(index:int) -> bool:
    if index < 0 or index >= len(space[0]):
        raise IndexError(f"{index} is out of space bounds")

    for row in space:
        if row[index] == "#":
            return False

    return True


def read_file(file_path:str) -> None:
    global space

    with open(file_path, 'r') as f:
        line = f.readline().strip("\n")
        while line != "":
            space.append([s for s in line])
            line = f.readline().strip("\n")


if __name__ == "__main__":
    main("../data/d11.txt")
