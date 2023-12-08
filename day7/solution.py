from utils import *
from functools import cmp_to_key


def get_name() -> str:
    return "day7"


def compare_hands(hand1: str, hand2: str, joker: bool) -> int:
    """
    :param hand1:
    :param hand2:
    :param joker:
    :return: 1 if hand1 > hand2
             -1 if hand1 < hand2
             0 if hand1 == hand2
    """

    hand1_data: tuple[str, int] = (hand1, get_hand_value(hand1, joker))
    hand2_data: tuple[str, int] = (hand2, get_hand_value(hand2, joker))

    if hand1_data[1] == hand2_data[1]:
        return compare_cards(hand1_data[0], hand2_data[0], joker)
    if hand1_data[1] > hand2_data[1]:
        return 1
    elif hand1_data[1] < hand2_data[1]:
        return -1
    return 0


def compare_cards(hand1_cards: str, hand2_cards: str, joker: bool) -> int:
    """
    :param hand1_cards:
    :param hand2_cards:
    :param joker:
    :return:  1 if hand1_cards > hand2_cards
              -1 if hand1_cards < hand2_cards
              0 if hand1_cards == hand2_cards
    """
    cards: str = "23456789TJQKA" if not joker else "J23456789TQKA"

    for index in range(len(hand1_cards)):
        print(f"{cards.index(hand1_cards[index])} vs {cards.index(hand2_cards[index])}")
        if cards.index(hand1_cards[index]) > cards.index(hand2_cards[index]):
            return 1
        elif cards.index(hand1_cards[index]) < cards.index(hand2_cards[index]):
            return -1

    return 0


def get_cards_freq(hand: str, joker: bool) -> dict[str, int]:
    freq: dict[str, int] = {}

    for card in hand:
        if card == "J" and joker:
            continue

        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1

    return freq


def get_hand_value(hand: str, joker: bool) -> int:

    print(f"{hand} - ", end="")

    joker_count: int = 0

    if hand == "JJJJJ":
        print("[N/J] 5 of a kind")
        return 6

    if joker:
        joker_count = hand.count("J")

        hand = hand.replace("J", "")

    if check_five_of_a_kind(hand, joker):
        print("[J] 5 of a kind")
        return 6

    if check_four_of_a_kind(hand, joker):
        if joker_count == 1:
            print("[J] 5 of a kind")
            return 6

        print("[N] 4 of a kind")
        return 5

    if check_full_house(hand, joker):
        print("[N] full house")
        return 4

    if check_three_of_a_kind(hand, joker):
        if joker_count == 1:
            print("[J] 4 of a kind")
            return 5

        if joker_count == 2:
            print("[J] 5 of a kind")
            return 6

        print("[N] 3 of a kind")
        return 3

    if check_two_pair(hand, joker):
        if joker_count == 1:
            print("[J] full house")
            return 4

        print("2 pair")
        return 2
    if check_one_pair(hand, joker):
        if joker_count == 1:
            print("[J] 3 of a kind")
            return 3

        if joker_count == 2:
            print("[J] 4 of a kind")
            return 5

        if joker_count == 3:
            print("[J] 5 of a kind")
            return 6

        print("[N } 1 pair")
        return 1

    if joker_count == 1:
        print("[J] 1 pair")
        return 1

    if joker_count == 2:
        print("[J] 3 of a kind")
        return 3

    if joker_count == 3:
        print("[J] 4 of a kind")
        return 5

    if joker_count == 4:
        print("[J] 5 of a kind")
        return 6

    print("[N] high card")
    return 0


def get_max_repeat(hand: str, joker: bool) -> int:
    return max(get_cards_freq(hand, joker).values())


def check_five_of_a_kind(hand: str, joker: bool) -> bool:
    return get_max_repeat(hand, joker) == 5


def check_four_of_a_kind(hand: str, joker: bool) -> bool:
    return get_max_repeat(hand, joker) == 4


def check_full_house(hand: str, joker: bool) -> bool:
    freq: dict[str, int] = get_cards_freq(hand, joker)

    found_three: bool = False
    found_two: bool = False

    for value in freq.values():
        if value == 3:
            found_three = True
        elif value == 2:
            found_two = True

    return found_three and found_two


def check_three_of_a_kind(hand: str, joker: bool) -> bool:
    return get_max_repeat(hand, joker) == 3


def check_two_pair(hand: str, joker: bool) -> bool:
    freq: dict[str, int] = get_cards_freq(hand, joker)

    found_two: bool = False

    for value in freq.values():
        if value == 2:
            if found_two:
                return True
            else:
                found_two = True

    return False


def check_one_pair(hand: str, joker: bool) -> bool:
    return get_max_repeat(hand, joker) == 2 and not check_two_pair(hand, joker)


def part1(lines: list[str]) -> str:
    hands: list[tuple[str, int]] = []

    for line in lines:
        hand, bet = line.split(" ")

        hands.append((hand, int(bet)))

    hands = sorted(hands, key=cmp_to_key(lambda hand1, hand2: compare_hands(hand1[0], hand2[0], False)), reverse=True)

    print(hands)

    result: int = 0

    for index in range(len(hands)):
        value = len(hands) - index

        result += hands[index][1] * value

    return str(result)


def part2(lines: list[str]) -> str:
    hands: list[tuple[str, int]] = []

    for line in lines:
        hand, bet = line.split(" ")

        hands.append((hand, int(bet)))

    hands = sorted(hands, key=cmp_to_key(lambda hand1, hand2: compare_hands(hand1[0], hand2[0], True)), reverse=True)

    print(hands)

    result: int = 0

    for index in range(len(hands)):
        value = len(hands) - index

        result += hands[index][1] * value

    return str(result)
