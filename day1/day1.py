from utils import *


def main():
    data_part1: str = read_file("day1/input")
    result_part1: int = 0

    data_part2 = add_spelled_out_numbers(data_part1)
    result_part2: int = 0

    for line in data_part1.splitlines():
        result_part1 += extract_number(line)

    for line in data_part2.splitlines():
        print(f"{line} -> {extract_number(line)}")
        result_part2 += extract_number(line)

    write_file("day1/part1.output", result_part1)
    write_file("day1/part2.output", result_part2)


def extract_number(string: str) -> int:
    first_digit: int = -1
    last_digit: int = -1
    for char in string:
        if char in "0123456789":
            int_char: int = int(char)

            if first_digit == -1:
                first_digit = int_char
                last_digit = int_char
            else:
                last_digit = int_char

    return first_digit * 10 + last_digit


def add_spelled_out_numbers(string: str) -> str:
    digits: dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for key in digits.keys():
        string = string.replace(key, key + digits[key] + key)

    return string


if __name__ == '__main__':
    main()
