from typing import List


def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    i: int = 0
    while i < len(string):
        if string[i] == '[':
            open_positions.append(i)
        else:
            close_positions.append(i)
        i += 1
    close_positions.reverse()
    matched_count: int = 0
    idx_close: int = 0
    total_close: int = len(close_positions)
    for element in open_positions:
        if idx_close < total_close and element < close_positions[idx_close]:
            matched_count += 1
            idx_close += 1
    return matched_count >= 2