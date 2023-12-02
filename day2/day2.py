from utils import *


def main():

    data: str = read_file("input")
    part1(data)
    part2(data)


def part2(data: str):
    write_file("part2.output", "")

    result: int = 0

    for game in data.splitlines():
        game_name: str = game.split(":")[0].strip()
        game_id: int = int(game_name.split(" ")[1].strip())
        print(f"Game ID: {game_id}")

        game_data = game.split(":")[1].strip()

        good: bool = True

        red: int = 0
        green: int = 0
        blue: int = 0

        for _data in game_data.split(";"):
            for data in _data.split(","):
                data = data.strip()
                number: int = int(data.split(" ")[0].strip())
                color: str = data.split(" ")[1].strip()

                print(f"{number} {color}")

                if color == "red":
                    red = max(red, number)
                elif color == "green":
                    green = max(green, number)
                elif color == "blue":
                    blue = max(blue, number)

            print(f"Red: {red}")
            print(f"Green: {green}")
            print(f"Blue: {blue}")

        result += red * green * blue
        append_file("part2.output", f"{red} {green} {blue}")

    append_file("part2.output", "")
    append_file("part2.output", result)


def part1(data: str):
    write_file("part1.output", "")

    result: int = 0

    max_red: int = 12
    max_green: int = 13
    max_blue: int = 14

    for game in data.splitlines():
        game_name: str = game.split(":")[0].strip()
        game_id: int = int(game_name.split(" ")[1].strip())
        print(f"Game ID: {game_id}")

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

                print(f"{number} {color}")

                if color == "red":
                    red += number
                elif color == "green":
                    green += number
                elif color == "blue":
                    blue += number

            print(f"Red: {red}/{max_red}")
            print(f"Green: {green}/{max_green}")
            print(f"Blue: {blue}/{max_blue}")

            if red > max_red or green > max_green or blue > max_blue:
                good = False

        if good:
            append_file("part1.output", str(game_id) + " ", False)
            result += game_id

        print()

    append_file("part1.output", "")
    append_file("part1.output", result)


if __name__ == '__main__':
    main()
