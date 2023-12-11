from utils import *
import sys
import resource


def part1(lines: list[str]) -> str:
    for index in range(len(lines)):
        lines[index] = f".{lines[index]}."

    start_position: tuple[int, int] = (0, 0)

    #                     N    E    S    W
    data_map: list[list[tuple[int, int, int, int]]] = []

    for line in lines:
        data: list[tuple[int, int, int, int]] = []
        for char in line:
            if char == ".":
                data.append((0, 0, 0, 0))
            elif char == "|":
                data.append((1, 0, 1, 0))
            elif char == "-":
                data.append((0, 1, 0, 1))
            elif char == "L":
                data.append((1, 1, 0, 0))
            elif char == "J":
                data.append((1, 0, 0, 1))
            elif char == "7":
                data.append((0, 0, 1, 1))
            elif char == "F":
                data.append((0, 1, 1, 0))
            elif char == "S":
                data.append((1, 1, 1, 1))

            else:
                data.append((0, 0, 0, 0))
        data_map.append(data)

        if "S" in line:
            start_position = (lines.index(line), line.index("S"))
            # break

    distances: list[list[int]] = []

    for distance_line in range(len(data_map)):
        distances.append([])
        for distance_column in range(len(data_map[distance_line])):
            distances[distance_line].append(0)

    distances[start_position[0]][start_position[1]] = 1

    bfs_part1(data_map, [start_position], distances)

    max_value: int = 0

    for distance_line in range(len(data_map)):
        for distance_column in range(len(data_map[distance_line])):
            max_value = max(max_value, distances[distance_line][distance_column])

    return str(max_value - 1)


def check_connection(data_map: list[list[tuple[int, int, int, int]]], current_position: tuple[int, int],
                     direction: tuple[int, int]) -> bool:
    current_data = data_map[current_position[0]][current_position[1]]
    target_data = data_map[current_position[0] + direction[0]][current_position[1] + direction[1]]

    if direction[0] == 1:
        if current_data[2] == 0 or target_data[0] == 0:
            return False
    elif direction[0] == -1:
        if current_data[0] == 0 or target_data[2] == 0:
            return False
    elif direction[1] == 1:
        if current_data[1] == 0 or target_data[3] == 0:
            return False
    elif direction[1] == -1:
        if current_data[3] == 0 or target_data[1] == 0:
            return False

    return True


def bfs_part1(data_map: list[list[tuple[int, int, int, int]]], check_positions: list[tuple[int, int]],
              distances: list[list[int]]) -> None:
    while True:
        if len(check_positions) == 0:
            return

        directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        new_check_positions: list[tuple[int, int]] = []

        for position in check_positions:
            data: tuple[int, int, int, int] = data_map[position[0]][position[1]]

            for index in range(4):
                if data[index] == 1:
                    new_position: tuple[int, int] = (
                        position[0] + directions[index][0], position[1] + directions[index][1])

                    if not check_connection(data_map, position, directions[index]):
                        continue

                    if data_map[new_position[0]][new_position[1]] == (0, 0, 0, 0):
                        continue

                    if distances[new_position[0]][new_position[1]] != 0:
                        continue

                    distances[new_position[0]][new_position[1]] = distances[position[0]][position[1]] + 1
                    new_check_positions.append(new_position)

        check_positions = new_check_positions


def pretty_print_map(data_map: list[list[tuple[int, int, int, int]]]) -> None:
    for line in data_map:
        for data in line:
            if data == (1, 0, 1, 0):
                print("│", end="")
                append_file("debug", "│")
            elif data == (0, 1, 0, 1):
                print("─", end="")
                append_file("debug", "─")
            elif data == (1, 1, 0, 0):
                print("└", end="")
                append_file("debug", "└")
            elif data == (1, 0, 0, 1):
                print("┘", end="")
                append_file("debug", "┘")
            elif data == (0, 0, 1, 1):
                print("┐", end="")
                append_file("debug", "┐")
            elif data == (0, 1, 1, 0):
                print("┌", end="")
                append_file("debug", "┌")
            elif data == (1, 1, 1, 1):
                print("┼", end="")
                append_file("debug", "┼")
            # elif data == (2, 2, 2, 2):
            #    print("#", end="")
            else:
                if data[0] == data[1] == data[2] == data[3] != 0:
                    print(data[0], end="")
                    append_file("debug", str(data[0]))
                else:
                    print(" ", end="")
                    append_file("debug", " ")

        print("")
        append_file("debug", "\n")


def part2(lines: list[str]) -> str:
    sys.setrecursionlimit(500000)

    for index in range(len(lines)):
        lines[index] = f".{lines[index]}."
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))

    start_position: tuple[int, int] = (0, 0)

    #                     N    E    S    W
    data_map: list[list[tuple[int, int, int, int]]] = []

    for line in lines:
        data: list[tuple[int, int, int, int]] = []
        for char in line:
            if char == ".":
                data.append((0, 0, 0, 0))
            elif char == "|":
                data.append((1, 0, 1, 0))
            elif char == "-":
                data.append((0, 1, 0, 1))
            elif char == "L":
                data.append((1, 1, 0, 0))
            elif char == "J":
                data.append((1, 0, 0, 1))
            elif char == "7":
                data.append((0, 0, 1, 1))
            elif char == "F":
                data.append((0, 1, 1, 0))
            elif char == "S":
                data.append((1, 1, 1, 1))
            elif char == "#":
                data.append((2, 2, 2, 2))
            else:
                data.append((0, 0, 0, 0))
        data_map.append(data)

        if "S" in line:
            start_position = (lines.index(line), line.index("S"))

    distances: list[list[int]] = []

    for distance_line in range(len(data_map)):
        distances.append([])
        for distance_column in range(len(data_map[distance_line])):
            distances[distance_line].append(0)

    distances[start_position[0]][start_position[1]] = 1
    bfs_part2(data_map, [start_position], distances)

    # Get an end position for the first pass of the dfs function
    max_value: int = 0
    max_value_position: tuple[int, int] = (0, 0)

    for distance_line in range(len(data_map)):
        for distance_column in range(len(data_map[distance_line])):
            if max_value < distances[distance_line][distance_column]:
                max_value = distances[distance_line][distance_column]
                max_value_position = (distance_line, distance_column)

    main_loop_1: list[tuple[int, int]] = dfs(data_map, start_position, max_value_position, [], [])
    main_loop_2: list[tuple[int, int]] = dfs(data_map, max_value_position, start_position, main_loop_1[1:], [])

    main_loop: list[tuple[int, int]] = main_loop_1 + main_loop_2[:-1]

    # Cleanup the map
    for line_index in range(len(data_map)):
        for column_index in range(len(data_map[line_index])):
            if (line_index, column_index) not in main_loop:
                data_map[line_index][column_index] = (0, 0, 0, 0)

    # Expand the map
    new_map: list[list[tuple[int, int, int, int]]] = []

    for line_index in range(len(data_map)):
        new_map.append([])
        for current_data in data_map[line_index]:
            new_map[line_index].append(current_data)
            new_map[line_index].append((0, 0, 0, 0))

    data_map = new_map[::]
    new_map = []

    for line_index in range(len(data_map)):
        new_map.append(data_map[line_index])
        new_map.append([(0, 0, 0, 0)] * len(data_map[line_index]))

    data_map = new_map[::]

    # Fill the gaps
    for line_index in range(len(data_map)):
        if line_index == 0 or line_index == len(data_map) - 1:
            continue

        for column_index in range(len(data_map[line_index])):
            new_data: tuple[int, int, int, int] = (0, 0, 0, 0)

            if column_index == 0 or column_index == len(data_map[line_index]) - 1:
                continue

            if data_map[line_index][column_index] != (0, 0, 0, 0):
                continue

            # N
            if data_map[line_index - 1][column_index][2] == 1:
                # E
                if data_map[line_index][column_index + 1][3] == 1:
                    new_data = (1, 1, 0, 0)
                # W
                elif data_map[line_index][column_index - 1][1] == 1:
                    new_data = (1, 0, 0, 1)
                # S
                elif data_map[line_index + 1][column_index][0] == 1:
                    new_data = (1, 0, 1, 0)
            # E
            elif data_map[line_index][column_index + 1][3] == 1:
                # W
                if data_map[line_index][column_index - 1][1] == 1:
                    new_data = (0, 1, 0, 1)
                # S
                elif data_map[line_index + 1][column_index][0] == 1:
                    new_data = (0, 1, 1, 0)
            # W
            elif data_map[line_index][column_index - 1][1] == 1:
                # S
                if data_map[line_index + 1][column_index][0] == 1:
                    new_data = (0, 0, 1, 1)

            data_map[line_index][column_index] = new_data

    fill_number: int = 2

    while True:
        found = 0
        for line_index in range(len(data_map)):
            for column_index in range(len(data_map[line_index])):
                line_data: tuple[int, int, int, int] = data_map[line_index][column_index]
                if line_data == (0, 0, 0, 0):
                    fill(data_map, (line_index, column_index), fill_number)

                    fill_number += 1
                    found = 1

                    break

            if found:
                break

        if not found:
            break

    result: int = 0

    for line_index in range(len(data_map)):
        for column_index in range(len(data_map[line_index])):
            if data_map[line_index][column_index] == (3, 3, 3, 3):
                if line_index % 2 == 0 and column_index % 2 == 0:
                    result += 1

    return str(result)


def fill(data_map: list[list[tuple[int, int, int, int]]], start_position: tuple[int, int], fill_number: int, interation:int =0) -> None:
    to_fill: list[tuple[int, int]] = [start_position]

    while True:
        if len(to_fill) == 0:
            break

        position = to_fill.pop()

        if position[0] < 0 or position[0] >= len(data_map):
            continue

        if position[1] < 0 or position[1] >= len(data_map[position[0]]):
            continue

        if data_map[position[0]][position[1]] != (0, 0, 0, 0):
            continue

        data_map[position[0]][position[1]] = (fill_number, fill_number, fill_number, fill_number)

        to_fill.append((position[0] - 1, position[1]))
        to_fill.append((position[0], position[1] + 1))
        to_fill.append((position[0] + 1, position[1]))
        to_fill.append((position[0], position[1] - 1))


def dfs(data_map: list[list[tuple[int, int, int, int]]], position: tuple[int, int],
        destination_position: tuple[int, int], visited: list[tuple[int, int]], path: list[tuple[int, int]]) \
        -> list[tuple[int, int]]:
    if len(path) == 0:
        path.append(position)
        visited.append(position)
    elif position == destination_position:
        return path

    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for index in range(4):
        new_position: tuple[int, int] = (position[0] + directions[index][0], position[1] + directions[index][1])

        if not check_connection(data_map, position, directions[index]):
            continue

        if new_position in visited:
            continue

        visited.append(new_position)
        path.append(new_position)

        result: list[tuple[int, int]] = dfs(data_map, new_position, destination_position, visited[::], path[::])

        if result:
            return result

        path.pop()
        visited.pop()

    return []


def bfs_part2(data_map: list[list[tuple[int, int, int, int]]], check_positions: list[tuple[int, int]],
              distances: list[list[int]]) -> None:
    while True:
        if len(check_positions) == 0:
            return

        directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        new_check_positions: list[tuple[int, int]] = []

        for position in check_positions:
            data: tuple[int, int, int, int] = data_map[position[0]][position[1]]

            for index in range(4):
                if data[index] == 1:
                    new_position: tuple[int, int] = (
                        position[0] + directions[index][0], position[1] + directions[index][1])

                    if not check_connection(data_map, position, directions[index]):
                        continue

                    if data_map[new_position[0]][new_position[1]] == (0, 0, 0, 0):
                        continue

                    if distances[new_position[0]][new_position[1]] != 0:
                        continue

                    distances[new_position[0]][new_position[1]] = distances[position[0]][position[1]] + 1
                    new_check_positions.append(new_position)

        check_positions = new_check_positions
