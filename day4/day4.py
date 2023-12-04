from utils import *
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def get_name() -> str:
    return "day4"


def part1(data) -> str:
    result: int = 0

    for card in data.splitlines():
        partial_result: int = 0

        card_data: str = card.split(":")[1]
        winning_data: str = card_data.split("|")[0]
        current_data: str = card_data.split("|")[1]

        winning_numbers: list[int] = [int(x) for x in winning_data.split(" ") if x != ""]
        current_numbers: list[int] = [int(x) for x in current_data.split(" ") if x != ""]

        for number in current_numbers:
            if number in winning_numbers:
                if partial_result == 0:
                    partial_result = 1
                else:
                    partial_result *= 2

        result += partial_result

    return str(result)


def part2(data) -> str:
    cards_data: list[str] = data.splitlines()
    number_of_cards: int = len(cards_data)

    cards: dict[int:int] = {}

    for index in range(1, number_of_cards + 1):
        cards[index] = 1

    for index in range(1, number_of_cards + 1):
        card = cards_data[index - 1]
        card_data: str = card.split(":")[1]
        winning_data: str = card_data.split("|")[0]
        current_data: str = card_data.split("|")[1]

        winning_numbers: list[int] = [int(x) for x in winning_data.split(" ") if x != ""]
        current_numbers: list[int] = [int(x) for x in current_data.split(" ") if x != ""]

        winning_count: int = 0

        for number in current_numbers:
            if number in winning_numbers:
                winning_count += 1

        for added_index in range(index + 1, index + winning_count + 1):
            cards[added_index] += cards[index]

    result: int = 0

    for card in cards.keys():
        result += cards[card]

    return str(result)


def pretty_print(lst: list[str]):
    for c in lst:
        print(c.split(":")[0].split(" ")[1], end=" ")
    print()
