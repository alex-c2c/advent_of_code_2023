#!/usr/bin/env python3

from timing import timeit
from dataclasses import dataclass, field


@dataclass
class Draw:
    red:int = 0
    green:int = 0
    blue:int = 0

    def __str__(self) -> str:
        return f"r:{self.red}, g:{self.green}, b:{self.blue}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(r:{self.red}, g:{self.green}, b:{self.blue})"


@dataclass
class Game:
    game_num:int = 0
    draws:list[Draw] = field(default_factory=list)


red_limit:int = 12
green_limit:int = 13
blue_limit:int = 14


@timeit
def main(file_path:str) -> None:
    sum:int = 0

    game_list:list[Game] = read_file(file_path)
    for game in game_list:
        if is_possible(game.draws):
            sum += game.game_num

    print(f"{sum = }")


def main_p2(file_path:str) -> None:
    sum:int = 0

    game_list:list[Game] = read_file(file_path)
    for game in game_list:
        higest_draw:Draw = get_highest_draw(game.draws)
        print(f"{game.draws = } | {higest_draw = }")

        sum += higest_draw.red * higest_draw.green * higest_draw.blue

    print(f"{sum = }")


def get_highest_draw(game_draws:list[Draw]) -> Draw:
    higest_draw = Draw()

    for draw in game_draws:
        if higest_draw.red == 0 or draw.red > higest_draw.red:
            higest_draw.red = draw.red

        if higest_draw.green == 0 or draw.green > higest_draw.green:
            higest_draw.green = draw.green

        if higest_draw.blue == 0 or draw.blue > higest_draw.blue:
            higest_draw.blue = draw.blue

    return higest_draw


def is_possible(game_draws:list[Draw]) -> bool:
    for draw in game_draws:
        if draw.red > red_limit:
            return False
        elif draw.green > green_limit:
            return False
        elif draw.blue > blue_limit:
            return False

    return True


def read_file(file_path:str) -> list[Game]:
    game_list:list[Game] = []

    with open(file_path, 'r') as f:
        line = f.readline()
        while line != "":
            game:Game = process_line(line)
            game_list.append(game)

            line = f.readline()

    return game_list


def clean_line(line:str) -> str:
    return line.strip("\n").replace("; ", ";").replace(": ", ":").replace(", ", ",") 


def process_line(line:str) -> Game:
    new_line = clean_line(line)

    game = Game()
    game_split = new_line.split(":")
    game.game_num = int(game_split[0].split(" ")[1])

    for draw_str in game_split[1].split(";"):
        draw = Draw()

        for color_str in draw_str.split(","):
            color_split = color_str.split(" ")
            #print(f"{color_split = }")
            if color_split[1] == "red":
                draw.red += int(color_split[0])
            elif color_split[1] == "green":
                draw.green += int(color_split[0])
            elif color_split[1] == "blue":
                draw.blue += int(color_split[0])

        game.draws.append(draw)
        
    return game


if __name__ == '__main__':
    #s = process_line("Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue")
    #print(f"{s = }")
    main_p2("../data/d2.txt")
