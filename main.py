from utils import *
import day5.day5 as current_day


def main():
    day_name = current_day.get_name()

    part1_input_small: str = read_file(f"{day_name}/input/part1.input.small")
    part1_input: str = read_file(f"{day_name}/input/input")

    part2_input_small: str = read_file(f"{day_name}/input/part2.input.small")
    part2_input: str = read_file(f"{day_name}/input/input")

    part1_output_small = current_day.part1(part1_input_small) if part1_input_small != "" else ""
    part1_output = current_day.part1(part1_input) if part1_input != "" else ""

    part2_output_small = current_day.part2(part2_input_small) if part2_input_small != "" else ""
    part2_output = current_day.part2(part2_input) if part2_input != "" else ""

    write_file(f"{day_name}/output/part1.output.small", part1_output_small)
    write_file(f"{day_name}/output/part1.output", part1_output)

    write_file(f"{day_name}/output/part2.output.small", part2_output_small)
    write_file(f"{day_name}/output/part2.output", part2_output)


if __name__ == '__main__':
    main()
