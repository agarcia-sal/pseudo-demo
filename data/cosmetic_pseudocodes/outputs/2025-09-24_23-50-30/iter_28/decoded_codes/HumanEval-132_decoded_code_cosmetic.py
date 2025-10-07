from typing import List, Tuple


def is_nested(string: str) -> bool:
    def gather_indices(pos: int, opens: List[int], closes: List[int]) -> Tuple[List[int], List[int]]:
        if pos == len(string):
            return opens, closes
        char = string[pos]
        o, c = gather_indices(pos + 1, opens, closes)
        if char == '[':
            return o + [pos], c
        else:
            return o, c + [pos]

    open_positions, close_positions = gather_indices(0, [], [])

    def reverse_in_place(lst: List[int], left: int, right: int) -> None:
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
            reverse_in_place(lst, left + 1, right - 1)

    reverse_in_place(close_positions, 0, len(close_positions) - 1)

    i = 0
    matched = 0
    max_close = len(close_positions)
    while i < len(open_positions):
        if matched < max_close and open_positions[i] < close_positions[matched]:
            matched += 1
            i += 1
        else:
            i += 1

    return matched >= 2