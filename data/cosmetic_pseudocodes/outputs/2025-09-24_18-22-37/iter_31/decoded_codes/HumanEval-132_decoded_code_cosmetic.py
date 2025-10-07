from typing import List


def is_nested(input_str: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    for idx, curr_char in enumerate(input_str):
        if curr_char == '[':
            open_positions.append(idx)
        else:
            close_positions.append(idx)

    close_positions.reverse()

    matched_pairs: int = 0
    close_ptr: int = 0
    total_closes: int = len(close_positions)

    for open_idx in open_positions:
        if close_ptr < total_closes and open_idx < close_positions[close_ptr]:
            matched_pairs += 1
            close_ptr += 1

    return matched_pairs >= 2