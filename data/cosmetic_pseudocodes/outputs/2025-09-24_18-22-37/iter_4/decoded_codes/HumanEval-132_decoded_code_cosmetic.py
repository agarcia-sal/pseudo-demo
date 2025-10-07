from typing import List

def is_nested(s: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '[':
            open_indices.append(i)
        else:
            close_indices.append(i)
        i += 1
    close_indices.reverse()
    nested_count = 0
    close_pos = 0
    closes_len = len(close_indices)
    idx = 0
    while idx < len(open_indices):
        if close_pos < closes_len:
            if open_indices[idx] < close_indices[close_pos]:
                nested_count += 1
                close_pos += 1
        idx += 1
    return nested_count >= 2