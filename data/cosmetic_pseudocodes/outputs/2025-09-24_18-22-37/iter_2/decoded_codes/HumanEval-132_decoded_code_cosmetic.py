from typing import List


def is_nested(input_string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    for i, ch in enumerate(input_string):
        if ch == '[':
            open_indices.append(i)
        else:
            close_indices.append(i)
    close_indices.reverse()
    matched_pairs = 0
    close_cursor = 0
    total_close = len(close_indices)
    for open_pos in open_indices:
        if close_cursor < total_close and open_pos < close_indices[close_cursor]:
            matched_pairs += 1
            close_cursor += 1
    return matched_pairs >= 2