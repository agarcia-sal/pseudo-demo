from typing import List


def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    for i in range(len(string)):
        if string[i] == '[':
            open_positions.append(i)
        else:
            close_positions.append(i)
    close_positions.reverse()

    matched_count = 0
    idx_to_check = 0
    while idx_to_check < len(close_positions) and matched_count < len(open_positions):
        if open_positions[matched_count] < close_positions[idx_to_check]:
            matched_count += 1
            idx_to_check += 1
        else:
            idx_to_check += 1
    return matched_count >= 2