from typing import List


def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    idx: int = 0
    while idx < len(string):
        if string[idx] == '[':
            open_positions.append(idx)
        else:
            close_positions.append(idx)
        idx += 1

    close_positions.sort(reverse=True)

    matched_count: int = 0
    close_idx: int = 0
    total_closes: int = len(close_positions)

    for open_pos in open_positions:
        if close_idx < total_closes and open_pos < close_positions[close_idx]:
            matched_count += 1
            close_idx += 1

    return matched_count >= 2