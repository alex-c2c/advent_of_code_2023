#!/usr/bin/env python3


schematic:tuple[str, ...] = ()


def main(file_path:str) -> None:
    global schematic
    schematic = read_file(file_path)
    print(f"{len(schematic) = }")
    print(f"{schematic[0]}")

    num_list:list[int] = []

    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if is_symbol(x, y):
                num_list += find_numbers_around(x, y)
                print(f"{schematic[y][x] = } - {num_list = }")

    sum:int = 0
    for num in num_list:
        sum += num

    print(f"{sum = }")


def main_p2(file_path:str) -> None:
    global schematic
    schematic = read_file(file_path)

    product_list:list[int] = []

    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if is_ast(x, y):
                num_list = find_numbers_around(x, y)
                if len(num_list) == 2:
                    product_list.append(num_list[0] * num_list[1])

    sum:int = 0
    for product in product_list:
        sum += product

    print(f"{sum = }")


def find_numbers_around(x:int, y:int) -> list[int]:
    global schematic
    num_list:list[int] = []

    if is_digit(x, y-1):
        num_list.append(convert_digits_to_num(get_digits_center(x, y-1)))
    else:
        if is_digit(x-1, y-1):
            num_list.append(convert_digits_to_num(get_digits_leftwards(x-1, y-1)))

        if is_digit(x+1, y-1):
            num_list.append(convert_digits_to_num(get_digits_rightwards(x+1, y-1)))

    if is_digit(x, y+1):
        num_list.append(convert_digits_to_num(get_digits_center(x, y+1)))
    else:
        if is_digit(x-1, y+1):
            num_list.append(convert_digits_to_num(get_digits_leftwards(x-1, y+1)))

        if is_digit(x+1, y+1):
            num_list.append(convert_digits_to_num(get_digits_rightwards(x+1, y+1)))

    if is_digit(x-1, y):
        num_list.append(convert_digits_to_num(get_digits_leftwards(x-1, y)))

    if is_digit(x+1, y):
        num_list.append(convert_digits_to_num(get_digits_rightwards(x+1, y)))

    return num_list


def convert_digits_to_num(char_list:list[str]) -> int:
    if len(char_list) == 0:
        return 0

    return int("".join(char_list))


def get_digits_leftwards(x:int, y:int) -> list[str]:
    global schematic

    char_list:list[str] = []

    while is_digit(x, y):
        char_list.append(schematic[y][x])
        x -= 1

    char_list.reverse()

    return char_list


def get_digits_rightwards(x:int, y:int) -> list[str]:
    global schematic

    char_list:list[str] = []

    while is_digit(x, y):
        char_list.append(schematic[y][x])
        x += 1

    return char_list


def get_digits_center(x:int, y:int) -> list[str]:
    global schematic

    char_list:list[str] = []

    if is_digit(x, y):
        char_list.append(schematic[y][x])

    leftward_list:list[str] = get_digits_leftwards(x-1, y)
    rightward_list:list[str] = get_digits_rightwards(x+1, y)

    char_list = leftward_list + char_list + rightward_list

    return char_list


def is_digit(x:int, y:int) -> bool:
    global schematic

    if y < 0 or y >= len(schematic):
        return False

    if x < 0 or x >= len(schematic[y]):
        return False

    return schematic[y][x].isdigit()


def is_ast(x:int, y:int) -> bool:
    global schematic

    if y < 0 or y >= len(schematic):
        return False

    if x < 0 or x >= len(schematic[y]):
        return False

    return schematic[y][x] == "*"

 
def is_symbol(x:int, y:int) -> bool:
    global schematic
    char:str = schematic[y][x]
    if not char.isdigit() and char != ".":
        return True

    return False


def read_file(file_path:str) -> tuple[str, ...]:
    with open(file_path, 'r') as f:
        return tuple(line.strip("\n") for line in f)


if __name__ == "__main__":
    main_p2("../data/d3.txt")

