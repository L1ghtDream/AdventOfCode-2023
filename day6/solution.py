from utils import *
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def get_name() -> str:
    return "day6"


def compute_distance(time: int, time_held: int) -> int:
    return (time - time_held) * time_held

"""

speed = time_held
time_left = time - time_held
distance = time_held * (time - time_held)


"""

def part1(data_lines: list[str]) -> str:
    times: list[int] = [int(x) for x in data_lines[0].split(":")[1].split(" ") if x != ""]
    distances: list[int] = [int(x) for x in data_lines[1].split(":")[1].split(" ") if x != ""]

    result = 1

    for index in range(len(times)):
        race_time = times[index]
        race_distance = distances[index]
        number_of_ways: int = 0

        for current_time in range(race_time):
            distance: int = compute_distance(race_time, current_time)

            if distance > race_distance:
                number_of_ways += 1

        result *= number_of_ways

    return str(result)


def part2(data_lines: list[str]) -> str:
    race_time: int = int(data_lines[0].split(":")[1].replace(" ", ""))
    race_distance: int = int(data_lines[1].split(":")[1].replace(" ", ""))

    result = 1

    number_of_ways: int = 0

    for current_time in range(race_time):
        distance: int = compute_distance(race_time, current_time)

        if distance > race_distance:
            number_of_ways += 1

    result *= number_of_ways

    return str(result)