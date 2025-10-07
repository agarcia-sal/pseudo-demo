from typing import List


def is_nested(alpha: str) -> bool:
    start_indices: List[int] = []
    end_indices: List[int] = []

    pos = 0
    while pos < len(alpha):
        current_char = alpha[pos]
        if current_char == '[':
            start_indices.append(pos)
        else:
            end_indices.append(pos)
        pos += 1

    end_indices.reverse()

    tally = 0
    idx_end = 0
    end_len = len(end_indices)

    for open_idx in start_indices:
        if idx_end < end_len and open_idx < end_indices[idx_end]:
            tally += 1
            idx_end += 1

    return tally >= 2