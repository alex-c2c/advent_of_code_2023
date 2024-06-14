#!/usr/bin/env python3

from dataclasses import dataclass, field
from functools import cmp_to_key


@dataclass
class Hand:
    cards:str = ""
    bid:int = 0


value_dict:dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


value_dict_v2:dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}



def main(file_path:str) -> None:
    hand_dict:dict[str, list[Hand]] = {}
    hand_dict["high_card"] = []
    hand_dict["one_pair"] = []
    hand_dict["two_pair"] = []
    hand_dict["three_of_a_kind"] = []
    hand_dict["full_house"] = []
    hand_dict["four_of_a_kind"] = []
    hand_dict["five_of_a_kind"] = []

    hands = read_file(file_path)
    for hand in hands:
        hand_dict[get_key_for_cards(hand.cards)].append(hand)

    full_list:list[Hand] = []
    for key in hand_dict:
        hand_dict[key].sort(key=cmp_to_key(cmp_cards))
        full_list += hand_dict[key]

    rank:int = 0
    winnings:int = 0
    for hand in full_list:
        rank += 1
        winnings += rank * hand.bid

    print(f"{winnings = }")


def main_p2(file_path:str) -> None:
    hand_dict:dict[str, list[Hand]] = {}
    hand_dict["high_card"] = []
    hand_dict["one_pair"] = []
    hand_dict["two_pair"] = []
    hand_dict["three_of_a_kind"] = []
    hand_dict["full_house"] = []
    hand_dict["four_of_a_kind"] = []
    hand_dict["five_of_a_kind"] = []

    hands = read_file(file_path)
    for hand in hands:
        hand_dict[get_key_for_cards_v2(hand.cards)].append(hand)

    full_list:list[Hand] = []
    for key in hand_dict:
        hand_dict[key].sort(key= cmp_to_key(cmp_cards_v2))
        full_list += hand_dict[key]

    for key in hand_dict:
        print(f"{key = } - {len(hand_dict[key]) = }")

    for hand in hand_dict["three_of_a_kind"]:
        if "J" in hand.cards:
            print(f"{hand = }")

    rank:int = 0
    winnings:int = 0
    for hand in full_list:
        rank += 1
        winnings += rank * hand.bid

    print(f"{winnings = }")


def cmp_cards_v2(a:Hand, b:Hand) -> int:
    for i in range(5):
        a_v = value_dict_v2[a.cards[i]]
        b_v = value_dict_v2[b.cards[i]]
        
        if a_v > b_v:
            return 1
        elif a_v < b_v:
            return -1

    return 0



def cmp_cards(a:Hand, b:Hand) -> int:
    for i in range(5):
        a_v = value_dict[a.cards[i]]
        b_v = value_dict[b.cards[i]]
        
        if a_v > b_v:
            return 1
        elif a_v < b_v:
            return -1

    return 0


def get_key_for_cards_v2(cards:str) -> str:
    card_dict:dict[str, int] = {}

    for card in cards:
        if card_dict.get(card, None) is None:
            card_dict[card] = 1
        else:
            card_dict[card] += 1

    j_cnt = card_dict.get("J", 0)

    if len(card_dict) == 1:
        # 5
        return "five_of_a_kind"
    elif len(card_dict) == 2:
        first, second = card_dict
        if card_dict[first] == 4 or card_dict[second] == 4:
            if j_cnt == 0:
                # 4 / 1
                return "four_of_a_kind"
            else:
                # 4 / J or J / 4
                return "five_of_a_kind"
        else:
            if j_cnt == 0:
                # 3 / 2
                return "full_house"
            else:
                # 3 / JJ or JJ / 3
                return "five_of_a_kind"
    elif len(card_dict) == 3:
        first, second, third = card_dict
        if card_dict[first] == 3 or card_dict[second] == 3 or card_dict[third] == 3:
            if j_cnt == 0:
                # 3 / 1 / 1
                return "three_of_a_kind"
            else:
                # 3 / J / 1 or JJJ / 1 / 1
                return "four_of_a_kind"
        else:
            # 2 / 2 / 1
            if j_cnt == 0:
                # 2 / 2 / 1
                return "two_pair"
            elif j_cnt == 1:
                # 2 / 2 / J
                return "full_house"
            elif j_cnt == 2:
                # JJ / 2 / 1
                return "four_of_a_kind"
    elif len(card_dict) == 4:
        if j_cnt == 0:
            # 2 / 1 / 1 / 1
            return "one_pair"
        elif j_cnt == 1 or j_cnt == 2:
            # 2 / J / 1 / 1
            return "three_of_a_kind"
    elif len(card_dict) == 5:
        # 1 / 1 / 1 / 1 / 1
        if j_cnt == 0:
            return "high_card"
        elif j_cnt == 1:
            return "one_pair"

    return "high_card"


def get_key_for_cards(cards:str) -> str:
    card_dict:dict[str, int] = {}

    for card in cards:
        if card_dict.get(card, None) is None:
            card_dict[card] = 1
        else:
            card_dict[card] += 1

    if len(card_dict) == 1:
        return "five_of_a_kind"
    elif len(card_dict) == 2:
        first, second = card_dict
        if card_dict[first] == 4 or card_dict[second] == 4:
            return "four_of_a_kind"
        else:
            return "full_house"
    elif len(card_dict) == 3:
        first, second, third = card_dict
        if card_dict[first] == 3 or card_dict[second] == 3 or card_dict[third] == 3:
            return "three_of_a_kind"
        else:
            return "two_pair"
    elif len(card_dict) == 4:
        return "one_pair"
    else:
        return "high_card"


def read_file(file_path:str) -> tuple[Hand, ...]:
    with open(file_path, 'r') as f:
        lines = f.readlines()

        return tuple(process_line(line.strip("\n")) for line in lines)


def process_line(line:str) -> Hand:
    line_split:list[str] = line.split(" ")

    return Hand(line_split[0], int(line_split[1]))


if __name__ == "__main__":
    main_p2("../data/d7.txt")
