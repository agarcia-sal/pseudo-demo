from typing import List


def is_nested(strng: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    for i, ch in enumerate(strng):
        if ch == '[':
            open_positions.append(i)
        else:
            close_positions.append(i)

    rev_close_positions: List[int] = close_positions[::-1]

    count_nested = 0
    pos_idx = 0
    total_close = len(rev_close_positions)

    while pos_idx < total_close:
        for op in open_positions:
            if pos_idx >= total_close:
                continue
            if op < rev_close_positions[pos_idx]:
                count_nested += 1
                pos_idx += 1

    return count_nested >= 2