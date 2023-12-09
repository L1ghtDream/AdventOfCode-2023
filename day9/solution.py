from utils import *


def part1(lines: list[str]) -> str:
    result: int = 0

    for line in lines:
        values_list: list[list[int]] = []

        values: list[int] = []
        for value in line.split(" "):
            values.append(int(value))

        values_list.append(values)

        while True:
            new_values: list[int] = []
            for index in range(len(values_list[-1]) - 1):
                new_values.append(values_list[-1][index + 1] - values_list[-1][index])

            values_list.append(new_values)

            for index in range(len(values_list[-1])):
                if values_list[-1][index] != 0:
                    break
            else:
                break

        for values in values_list:
            values.append(0)

        for index in range(len(values_list) - 2, -1, -1):
            values_list[index][-1] = values_list[index][-2] + values_list[index + 1][-1]

        result += values_list[0][-1]

    return str(result)


def part2(lines: list[str]) -> str:
    result: int = 0

    for line in lines:
        values_list: list[list[int]] = []

        values: list[int] = []
        for value in line.split(" "):
            values.append(int(value))

        values_list.append(values)

        while True:
            new_values: list[int] = []
            for index in range(len(values_list[-1]) - 1):
                new_values.append(values_list[-1][index + 1] - values_list[-1][index])

            values_list.append(new_values)

            for index in range(len(values_list[-1])):
                if values_list[-1][index] != 0:
                    break
            else:
                break

        for index in range(len(values_list)):
            values_list[index] = [0] + values_list[index]

        for index in range(len(values_list) - 2, -1, -1):
            values_list[index][0] = values_list[index][1] - values_list[index + 1][0]

        result += values_list[0][0]

    return str(result)
