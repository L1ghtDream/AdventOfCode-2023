from utils import *
import day2.day2 as current_day


def main():
    part1_input: str = read_file(f"{current_day.get_name()}/input/part1.input.small")
    part2_input: str = read_file(f"{current_day.get_name()}/input/part2.input.small")
    input: str = read_file(f"{current_day.get_name()}/input/input")

    part1_output_small = current_day.part1(part1_input, )
    part1_output = current_day.part1(input)

    part2_output_small = current_day.part2(part2_input)
    part2_output = current_day.part2(input)

    write_file(f"{current_day.get_name()}/output/part1.output.small", part1_output_small)
    write_file(f"{current_day.get_name()}/output/part1.output", part1_output)
    write_file(f"{current_day.get_name()}/output/part2.output.small", part2_output_small)
    write_file(f"{current_day.get_name()}/output/part2.output", part2_output)


if __name__ == '__main__':
    main()
