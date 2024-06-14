#!/usr/bin/env python3

from timing import timeit

@timeit
def main() -> None:
    stack:list[str] = []

    with open("../data/d1.txt", 'r') as f:
        line = f.readline()
        while line != '':
            num_string = extract_num_string(line)
            stack.append(num_string)
            line = f.readline()

    total:int = 0
    for s in stack:
        total += int(s)

    print(f"{total = }")


# day 1 part 1
def extract_num_string(line:str) -> str:
    line_len:int = len(line)
    f_index:int = 0
    b_index:int = line_len - 1

    while True:
        if line[f_index].isdigit() and line[b_index].isdigit():
            return line[f_index] + line[b_index]

        if not line[f_index].isdigit():
            f_index += 1

            if f_index >= line_len:
                raise IndexError(f"")

        if not line[b_index].isdigit():
            b_index -= 1

            if b_index < 0:
                raise IndexError(f"")


# day 1 part 2
def extract_num(line:str) -> str:
    check_dict:dict[str, str] = {}
    check_dict["one"] = "1"
    check_dict["two"] = "2"
    check_dict["three"] = "3"
    check_dict["four"] = "4"
    check_dict["five"] = "5"
    check_dict["six"] = "6"
    check_dict["seven"] = "7"
    check_dict["eight"] = "8"
    check_dict["nine"] = "9"

    num_str_list:list[str] = []
    line_len:int = len(line)

    index:int = 0
    while True:
        if index >= line_len:
            break

        c:str = line[index]
        #print(f"checking {c = }")
        if c.isdigit():
            num_str_list.append(c)

        else:
            for key in check_dict:
                if len(key) + index > line_len:
                    continue
                else:
                    sub_str:str = line[index:index + len(key)]
                    #print(f"{line = } - {index = } - {len(key) = } - {sub_str = }")
                    if sub_str == key:
                        num_str_list.append(check_dict[key])
                        break
        index += 1

    #print(f"{line = } - {num_str_list = } - {num_str_list[0] + num_str_list[-1]}")

    return num_str_list[0] + num_str_list[-1]


if __name__ == '__main__':
    main()
