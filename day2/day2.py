from utils import *


def get_name() -> str:
    return "day2"


def part1(data, output_file):
    result: int = 0

    max_red: int = 12
    max_green: int = 13
    max_blue: int = 14

    for game in data.splitlines():
        game_name: str = game.split(":")[0].strip()
        game_id: int = int(game_name.split(" ")[1].strip())

        game_data = game.split(":")[1].strip()

        good: bool = True

        for _data in game_data.split(";"):
            red: int = 0
            green: int = 0
            blue: int = 0

            for data in _data.split(","):
                data = data.strip()
                number: int = int(data.split(" ")[0].strip())
                color: str = data.split(" ")[1].strip()

                if color == "red":
                    red += number
                elif color == "green":
                    green += number
                elif color == "blue":
                    blue += number

            if red > max_red or green > max_green or blue > max_blue:
                good = False

        if good:
            result += game_id

    write_file(output_file, result)


def part2(data, output_file):
    result: int = 0

    for game in data.splitlines():
        game_data = game.split(":")[1].strip()

        red: int = 0
        green: int = 0
        blue: int = 0

        for _data in game_data.split(";"):
            for data in _data.split(","):
                data = data.strip()
                number: int = int(data.split(" ")[0].strip())
                color: str = data.split(" ")[1].strip()

                if color == "red":
                    red = max(red, number)
                elif color == "green":
                    green = max(green, number)
                elif color == "blue":
                    blue = max(blue, number)

        result += red * green * blue

    write_file(output_file, result)

