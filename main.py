from utils import *
import sys
import importlib
import os


def get_last_day() -> int:
    max_day: int = 0

    for dir in os.listdir("."):
        if not os.path.isdir(dir):
            continue

        if not dir.startswith("day"):
            continue

        if not dir[3:].isnumeric():
            continue

        day: int = int(dir[3:])
        max_day = max(max_day, day)

    return max_day


def main():
    number_of_arguments: int = len(sys.argv) - 1
    arguments: list[str] = sys.argv[1:number_of_arguments]

    if number_of_arguments == 0:
        day: int = get_last_day()
    else:
        day: int = int(arguments[0])

    current_day = importlib.import_module(f"day{day}.solution")

    day_name = current_day.get_name()

    part1_input_small: str = read_file(f"{day_name}/input/part1.input.small")
    part1_input: str = read_file(f"{day_name}/input/input")

    part2_input_small: str = read_file(f"{day_name}/input/part2.input.small")
    part2_input: str = read_file(f"{day_name}/input/input")

    part1_output_small = current_day.part1(part1_input_small.splitlines()) if part1_input_small != "" else ""
    part1_output = current_day.part1(part1_input.splitlines()) if part1_input != "" else ""

    part2_output_small = current_day.part2(part2_input_small.splitlines()) if part2_input_small != "" else ""
    part2_output = current_day.part2(part2_input.splitlines()) if part2_input != "" else ""

    write_file(f"{day_name}/output/part1.output.small", part1_output_small)
    write_file(f"{day_name}/output/part1.output", part1_output)

    write_file(f"{day_name}/output/part2.output.small", part2_output_small)
    write_file(f"{day_name}/output/part2.output", part2_output)


if __name__ == '__main__':
    main()
