from typing import List


def is_nested(string: str) -> bool:
    opening_positions: List[int] = []
    closing_positions: List[int] = []

    def helper(i: int) -> None:
        if i == len(string):
            return
        if string[i] == '[':
            opening_positions.append(i)
        else:
            closing_positions.append(i)
        helper(i + 1)

    helper(0)
    closing_positions.reverse()
    idx_closing = 0
    total_closing = len(closing_positions)
    nested_count = 0

    def check_positions(j: int) -> None:
        nonlocal idx_closing, nested_count
        if j == len(opening_positions):
            return
        open_pos = opening_positions[j]
        if idx_closing < total_closing and open_pos < closing_positions[idx_closing]:
            nested_count += 1
            idx_closing += 1
        check_positions(j + 1)

    check_positions(0)
    return nested_count >= 2