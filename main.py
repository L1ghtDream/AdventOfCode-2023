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
    arguments: list[str] = sys.argv[1:]

    if number_of_arguments == 0:
        day_number: int = get_last_day()
    else:
        day_number: int = int(arguments[0])

    day_name = f"day{day_number}"
    current_day = importlib.import_module(f"{day_name}.solution")

    for file in os.listdir(f"{day_name}/input/part1/"):
        if not file.endswith(".input"):
            continue

        partial_input: str = read_file(f"{day_name}/input/part1/{file}")
        partial_output: str = current_day.part1(partial_input.splitlines()) if partial_input != "" else ""
        write_file(f"{day_name}/output/part1/{file.replace('.input', '.output')}", partial_output)

    part1_input: str = read_file(f"{day_name}/input/part1/input")
    part1_output = current_day.part1(part1_input.splitlines()) if part1_input != "" else ""
    write_file(f"{day_name}/output/part1/output", part1_output)

    for file in os.listdir(f"{day_name}/input/part2/"):
        if not file.endswith(".input"):
            continue

        partial_input: str = read_file(f"{day_name}/input/part2/{file}")
        partial_output: str = current_day.part2(partial_input.splitlines()) if partial_input != "" else ""
        write_file(f"{day_name}/output/part2/{file.replace('.input', '.output')}", partial_output)

    part2_input: str = read_file(f"{day_name}/input/part2/input")
    part2_output = current_day.part2(part1_input.splitlines()) if part2_input != "" else ""
    write_file(f"{day_name}/output/part2/output", part2_output)


if __name__ == '__main__':
    main()
