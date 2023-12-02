from utils import *
import day2.day2 as current_day


def main():
    part1_input: str = read_file(f"{current_day.get_name()}/input/part1.input.small")
    part2_input: str = read_file(f"{current_day.get_name()}/input/part2.input.small")
    input: str = read_file(f"{current_day.get_name()}/input/input")

    current_day.part1(part1_input, f"{current_day.get_name()}/output/part1.output.small")
    current_day.part1(input, f"{current_day.get_name()}/output/part1.output")

    current_day.part2(part2_input, f"{current_day.get_name()}/output/part2.output.small")
    current_day.part2(input, f"{current_day.get_name()}/output/part2.output")


if __name__ == '__main__':
    main()
