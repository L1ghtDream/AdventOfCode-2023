from utils import *




def part1(lines: list[str]) -> str:
    result: int = 0

    for line in lines:
        result += extract_number(line)

    return str(result)


def part2(lines: list[str]) -> str:
    result: int = 0

    for line in add_spelled_out_numbers(lines):
        result += extract_number(line)

    return str(result)


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


def add_spelled_out_numbers(lines: list[str]) -> list[str]:
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
        lines = replace_all(lines, key, key + digits[key] + key)

    return lines
