from utils import *
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def get_name() -> str:
    return "day5"


def part1(data) -> str:
    data_lines: list[str] = [x for x in data.splitlines() if x != ""]

    raw_seeds: str = data_lines[0].split(":")[1].strip()
    seeds: list[int] = [int(x) for x in raw_seeds.split(" ") if x != ""]

    data_lines = data_lines[1:]

    maps: list[list[OffsetRange]] = []
    conversions: list[OffsetRange] = []

    for line in data_lines:
        if "map" in line:
            maps.append(conversions)
            conversions = []
            continue

        destination, source, amount = line.split(" ")

        source: int = int(source)
        destination: int = int(destination)
        amount: int = int(amount)

        offset: int = destination - source
        conversions.append(OffsetRange(source, source + amount, offset))

    maps.append(conversions)
    to_check: list[int] = seeds.copy()

    for map in maps:
        after_conversion: list[int] = []

        for number in to_check:
            for conversion in map:
                if conversion.margins[0][0] <= number <= conversion.margins[0][1]:
                    after_conversion.append(number + conversion.offset)
                    break
            else:
                after_conversion.append(number)

        to_check = after_conversion.copy()

    return str(min(to_check))


class OffsetRange:
    margins: list[tuple[int, int]]
    offset: int

    def __init__(self, start: int, end: int, offset: int):
        self.margins = [(start, end)]
        self.offset = offset

    def copy(self):
        output = OffsetRange(0, 0, self.offset)
        output.margins = self.margins.copy()

        return output

    def minus(self, other):
        output: OffsetRange = OffsetRange(0, 0, self.offset)
        output.margins.pop()

        for margin in self.margins:
            for other_margin in other.margins:
                start: int = margin[0]
                end: int = margin[1]

                other_start: int = other_margin[0]
                other_end: int = other_margin[1]

                if other_start <= start <= other_end and other_start <= end <= other_end:
                    continue

                if start <= other_start <= end <= other_end:
                    output.margins.append((start, other_start))
                    continue

                if other_start <= start <= other_end <= end:
                    output.margins.append((other_end, end))
                    continue

                if start <= other_start <= other_end <= end:
                    output.margins.append((start, other_start))
                    output.margins.append((other_end, end))
                    continue

                output.margins.append(margin)

        return output

    def intersect(self, other):
        intersected_margins: list[tuple[int, int]] = []

        for margin in self.margins:
            for other_margin in other.margins:
                start: int = max(margin[0], other_margin[0])
                end: int = min(margin[1], other_margin[1])

                if start > end:
                    continue

                intersected_margins.append((start, end))

        output: OffsetRange = OffsetRange(0, 0, self.offset)
        output.margins = intersected_margins

        return output

    def apply_offset(self):
        margins = []

        for margin in self.margins:
            margins.append((margin[0] + self.offset, margin[1] + self.offset))

        self.margins = margins
        self.offset = 0

    def __str__(self):
        if self.offset == 0:
            return f"{{{self.margins}}}"
        return f"{{{self.margins}, {self.offset})}}"

    def __repr__(self):
        return str(self)


def part2(data) -> str:
    data_lines: list[str] = [x for x in data.splitlines() if x != ""]

    raw_seeds: str = data_lines[0].split(":")[1].strip()
    seeds_data: list[int] = [int(x) for x in raw_seeds.split(" ") if x != ""]
    seeds: list[OffsetRange] = []

    for index in range(0, len(seeds_data), 2):
        start = seeds_data[index]
        size = seeds_data[index + 1]

        seeds.append(OffsetRange(start, start + size, 0))

    data_lines = data_lines[1:]
    maps: list[list[OffsetRange]] = []
    conversions: list[OffsetRange] = []

    for line in data_lines:
        if "map" in line:
            maps.append(conversions)
            conversions = []
            continue

        destination, source, amount = line.split(" ")

        source: int = int(source)
        destination: int = int(destination)
        amount: int = int(amount)

        offset = destination - source
        conversions.append(OffsetRange(source, source + amount, offset))

    maps.append(conversions)
    to_check: list[OffsetRange] = seeds.copy()

    for map in maps:
        after_conversion: list[OffsetRange] = []

        for check_range in to_check:
            check_range: OffsetRange = check_range.copy()
            converted: list[OffsetRange] = []

            for conversion in map:
                output: OffsetRange = conversion.copy().intersect(check_range)

                if output is not None and len(output.margins) != 0:
                    converted.append(output.copy())
                    output.apply_offset()
                    after_conversion.append(output)

            for conversion in converted:
                check_range = check_range.minus(conversion)

            if check_range is not None and len(check_range.margins) != 0:
                after_conversion.append(check_range)

        to_check = after_conversion.copy()

    minimum: int = 10000000000

    for check_range in to_check:
        for margin in check_range.margins:
            minimum = min(minimum, margin[0])

    return str(minimum)
