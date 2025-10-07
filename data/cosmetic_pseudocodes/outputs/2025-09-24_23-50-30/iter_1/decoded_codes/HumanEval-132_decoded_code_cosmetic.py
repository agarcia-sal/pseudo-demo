from typing import List


def is_nested(string: str) -> bool:
    opening_positions: List[int] = []
    closing_positions: List[int] = []

    for idx, char in enumerate(string):
        if char == '[':
            opening_positions.append(idx)
        else:
            closing_positions.append(idx)

    closing_positions.reverse()

    matched_pairs = 0
    close_pos_idx = 0
    max_close = len(closing_positions)

    for open_pos in opening_positions:
        if close_pos_idx < max_close and open_pos < closing_positions[close_pos_idx]:
            matched_pairs += 1
            close_pos_idx += 1

    return matched_pairs >= 2