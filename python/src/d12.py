#!/usr/bin/env python3


def get_combination(hotspring:str, info:tuple[int, ...]) -> int:
    print(f"{hotspring = } | {info = }")
    combi:int = 0
    q_cnt:int = hotspring.count("?")
    damage_count = sum(list(info))
    open_damage_count = hotspring.count("#")
    diff = damage_count - open_damage_count

    for x in range(2**q_cnt):
        bstr = str(bin(x))[2:].zfill(q_cnt)
        if bstr.count("0") != diff:
            continue

        slist:list = [s for s in bstr.replace("0", "#").replace("1", ".")]
        #print(f"{slist = }")
        new_hotspring:str = ""
        for i in range(len(hotspring)):
            if hotspring[i] != "?":
                new_hotspring = new_hotspring + hotspring[i]
            else:
                new_hotspring = new_hotspring + slist.pop(0)

        if is_valid(new_hotspring, info):
            combi += 1

    return combi


def is_valid(hotspring:str, check_info:tuple[int, ...]) -> bool:
    #print(f"{hotspring = }")
    #hsl:list[str] = hotspring.split(".")
    #hst:tuple[int, ...] = tuple(len(s) for s in hsl)
    #print(f"{hsl = }, {hst = }")
    #print(f"{hst == check_info = }")
    return tuple(len(s) for s in hotspring.split(".") if s != "")  == check_info


def main(file_path:str) -> None:
    data:tuple[tuple[str, tuple[int, ...]], ...] = read_file(file_path)

    sum:int = 0
    for d in data[:1]:
        sum += get_combination(d[0]*2, d[1]*2)

    print(f"{sum = }")

    #print(f"{get_combination(".??.???...", (2, 2)) = }")

def read_file(file_path:str) -> tuple[tuple[str, tuple[int, ...]], ...]:
    with open (file_path, 'r') as f:
        lines = f.readlines()
        return tuple(process_line(line.strip("\n")) for line in lines)


def process_line(line:str) -> tuple[str, tuple[int, ...]]:
    ls = line.split(" ")
    return (ls[0], tuple(int(c) for c in ls[1].split(",")))


if __name__ == "__main__":
    main("../data/d12.txt")
