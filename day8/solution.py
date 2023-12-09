from utils import *
from functools import reduce
from math import gcd


def part1(lines: list[str]) -> str:
    instructions: str = lines[0]

    lines = lines[2:]

    directions: dict[str, tuple[str, str]] = {}

    for line in lines:
        position = line.split("=")[0].strip()
        left = line.split("=")[1].split(",")[0].replace("(", "").strip()
        right = line.split("=")[1].split(",")[1].replace(")", "").strip()

        directions[position] = (left, right)

    index: int = 0
    count: int = 0
    position: str = "AAA"

    while True:
        index = index % len(instructions)

        instruction = instructions[index]

        if instruction == "L":
            position = directions[position][0]
        else:
            position = directions[position][1]

        index += 1
        count += 1

        if position == "ZZZ":
            break

    return str(count)


def part2(lines: list[str]) -> str:
    instructions: str = lines[0]

    lines = lines[2:]

    directions: dict[str, tuple[str, str]] = {}

    for line in lines:
        position = line.split("=")[0].strip()
        left = line.split("=")[1].split(",")[0].replace("(", "").strip()
        right = line.split("=")[1].split(",")[1].replace(")", "").strip()

        directions[position] = (left, right)

    index: int = 0
    count: int = 0

    positions: list[str] = []

    for position in directions:
        if position.endswith("A"):
            positions.append(position)

    counts: list[int] = [0] * len(positions)

    while True:
        index = index % len(instructions)

        instruction = instructions[index]

        for position_index in range(len(positions)):
            position = positions[position_index]

            if instruction == "L":
                positions[position_index] = directions[position][0]
            else:
                positions[position_index] = directions[position][1]

        index += 1
        count += 1

        append_file("debug", f"[{count}] {str(positions)}")
        append_file("debug", "\n")

        for position_index in range(len(positions)):
            if counts[position_index] != 0:
                continue

            position = positions[position_index]

            if position.endswith("Z"):
                counts[position_index] = count

        for position_index in range(len(positions)):
            if counts[position_index] == 0:
                break
        else:
            break

    result: int = lcm_of_list(counts)

    return str(result)


def lcm_of_list(numbers):
    def lcm(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm, numbers)
