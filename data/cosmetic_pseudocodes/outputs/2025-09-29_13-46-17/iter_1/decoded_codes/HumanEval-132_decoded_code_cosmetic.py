from typing import List

def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    for i, ch in enumerate(string):
        if ch == '[':
            open_indices.append(i)
        else:
            close_indices.append(i)
    close_indices.reverse()
    matched_pairs = 0
    close_pos = 0
    close_len = len(close_indices)
    for open_idx in open_indices:
        if close_pos < close_len and open_idx < close_indices[close_pos]:
            matched_pairs += 1
            close_pos += 1
    return matched_pairs >= 2