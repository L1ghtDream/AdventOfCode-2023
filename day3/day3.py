from utils import *
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def get_name() -> str:
    return "day3"


def part1(data) -> str:
    result: int = 0

    symbols: set[str] = generate_symbols(data)
    lines: list[str] = data.splitlines()

    data_processed: list[str] = []

    for line in lines:
        data_processed.append(".." + line + "..")

    lines = data_processed

    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))

    for line_index in range(1, len(lines) - 1):
        line: str = lines[line_index]
        start: int = -1
        near_symbol = False

        for index in range(1, len(line)):
            if line[index].isdigit():
                if start == -1:
                    start = index

                directions: list[int] = [-1, 0, 1]

                for x in directions:
                    for y in directions:
                        if x == 0 and y == 0:
                            continue
                        if lines[line_index + y][index + x] in symbols:
                            near_symbol = True
            else:
                if start != -1:
                    string: str = line[start:index]
                    if near_symbol:
                        result += int(string)

                    start = -1
                    near_symbol = False

    return str(result)


def part2(data) -> str:
    result: int = 0

    symbols: set[str] = generate_symbols(data)
    lines: list[str] = data.splitlines()

    data_processed: list[str] = []

    for line in lines:
        data_processed.append(".." + line + "..")

    lines = data_processed

    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))
    gears: dict[set:list[int]] = {}

    for line_index in range(1, len(lines) - 1):
        line: str = lines[line_index]
        start: int = -1
        nearby_gears: list[set[int:int]] = []

        for index in range(1, len(line)):
            if line[index].isdigit():
                if start == -1:
                    start = index

                directions: list[int] = [-1, 0, 1]

                for x in directions:
                    for y in directions:
                        if x == 0 and y == 0:
                            continue
                        if lines[line_index + y][index + x] == "*":
                            gear = (line_index + y, index + x)
                            if gear not in nearby_gears:
                                nearby_gears.append((line_index + y, index + x))
            else:
                if start != -1:
                    string: str = line[start:index]

                    if nearby_gears:
                        data = int(string)

                        for nearby_gear in nearby_gears:
                            current_connections: list[int] = gears.get(nearby_gear, [])
                            current_connections.append(data)

                            gears[nearby_gear] = current_connections

                    start = -1
                    nearby_gears = []

    for gear in gears.keys():
        connections: list[int] = gears[gear]

        if len(connections) == 2:
            result += connections[0] * connections[1]

    return str(result)


def generate_symbols(data: str) -> set[str]:
    data = data.replace("\n", "").replace(".", "")

    for number in range(0, 10):
        data = data.replace(str(number), "")

    return set(data)
