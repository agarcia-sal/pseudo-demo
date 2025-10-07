from typing import List

def is_nested(input_string: str) -> bool:
    list_openings: List[int] = []
    list_closings: List[int] = []
    idx_outer: int = 0

    while idx_outer != len(input_string):
        ch = input_string[idx_outer]
        if ch == '[':
            list_openings.append(idx_outer)
        else:
            list_closings.append(idx_outer)
        idx_outer += 1

    reversed_closings: List[int] = []
    pos_rev: int = len(list_closings) - 1
    while pos_rev >= 0:
        reversed_closings.append(list_closings[pos_rev])
        pos_rev -= 1

    accumulator: int = 0
    cursor: int = 0
    max_cursor: int = len(reversed_closings)
    for open_idx in list_openings:
        if cursor < max_cursor and not (open_idx >= reversed_closings[cursor]):
            accumulator += 1
            cursor += 1
    return not (accumulator < 2)