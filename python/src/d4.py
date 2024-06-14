#!/usr/bin/env python3

from dataclasses import dataclass, field


@dataclass
class Card:
    card_num:int = 0
    winning_numbers:set[int]  = field(default_factory=set)
    my_numbers:set[int] = field(default_factory=set)
    intersect:set[int] = field(default_factory=set)


count_dict:dict[int, int] = {}


def main(file_path:str) -> None:
    cards:tuple[Card, ...] = read_file(file_path)
    
    sum:int = 0

    for card in cards:
        print(f"{card.card_num = } - {card.winning_numbers = } - {card.my_numbers = }")
        print(f"{card.intersect = }") 
        card_points:int = 0
        if len(card.intersect) > 0:
            card_points = 2 ** (len(card.intersect) - 1)

        sum += card_points

    print(f"{sum = }")


def main_p2(file_path:str) -> None:
    global count_dict
    cards:tuple[Card, ...] = read_file(file_path)

    for card in cards:
        add_count(card.card_num, 1)

        win_count = len(card.intersect)

        print(f"{card.card_num = } - {len(card.intersect) = }")
        if win_count > 0:
            for x in range(card.card_num + 1, card.card_num + win_count + 1):
                add_count(x, count_dict[card.card_num])

        print(f"{count_dict = }")
        print(f"-----------")

    sum:int = 0
    for key in count_dict:
        sum += count_dict[key]

    print(f"{sum = }")


def add_count(card_num:int, count:int) -> None:
    global count_dict

    if count_dict.get(card_num, None) is None:
        count_dict[card_num] = count
    else:
        count_dict[card_num] += count


def read_file(file_path:str) -> tuple[Card, ...]:
    with open(file_path, 'r') as f:
        return tuple(process_line(line.strip("\n")) for line in f.readlines())


def read_file_v2(file_path:str) -> dict[int, Card]:
    card_dict:dict[int, Card] = {}

    with open(file_path, 'r') as f:
        line = f.readline()
        while line != "":
            card:Card = process_line(line.strip("\n"))
            card_dict[card.card_num] = card
            line = f.readline()

    return card_dict


def process_line(line:str) -> Card:
    card_split:list[str] = line.split(":")

    card = Card()
    card_num_list = [s for s in card_split[0].split(" ") if s != ""]
    card.card_num = int(card_num_list[1])
    
    number_split = card_split[1].split("|")
    card.winning_numbers = set(int(digits) for digits in number_split[0].split(" ") if digits != "")
    card.my_numbers = set(int(digits) for digits in number_split[1].split(" ") if digits != "")
    card.intersect = card.winning_numbers.intersection(card.my_numbers)

    if len(card.winning_numbers) != 10:
        raise ValueError(f"{card.card_num =} winning_numbers({len(card.winning_numbers)}) is not 10")

    if len(card.my_numbers) != 25:
        raise ValueError(f"{card.card_num = } my_numbers({len(card.my_numbers)}) is not 25")

    return card


if __name__ == "__main__":
    main_p2("../data/d4.txt")
