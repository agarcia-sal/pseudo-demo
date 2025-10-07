from typing import List


def is_nested(string: str) -> bool:
    start_positions: List[int] = []
    end_positions: List[int] = []
    iterator = 0

    while iterator < len(string):
        if string[iterator] == '[':
            start_positions.append(iterator)
        else:
            end_positions.append(iterator)
        iterator += 1

    end_positions.reverse()

    matched = 0
    current_end = 0
    total_ends = len(end_positions)

    for start_index in start_positions:
        if current_end < total_ends and start_index < end_positions[current_end]:
            matched += 1
            current_end += 1

    return matched >= 2