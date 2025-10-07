from typing import List


def is_nested(strng: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    pos_iter: int = 0

    # Separate indices of '[' and other chars
    while pos_iter < len(strng):
        if strng[pos_iter] == '[':
            open_positions.append(pos_iter)
        else:
            close_positions.append(pos_iter)
        pos_iter += 1

    def reverse_list(lst: List[int]) -> None:
        left_idx = 0
        right_idx = len(lst) - 1
        while left_idx < right_idx:
            lst[left_idx], lst[right_idx] = lst[right_idx], lst[left_idx]
            left_idx += 1
            right_idx -= 1

    reverse_list(close_positions)

    matched_count: int = 0
    close_idx: int = 0
    max_close_idx: int = len(close_positions)

    for open_idx in open_positions:
        if close_idx < max_close_idx and open_idx < close_positions[close_idx]:
            matched_count += 1
            close_idx += 1

    return matched_count >= 2