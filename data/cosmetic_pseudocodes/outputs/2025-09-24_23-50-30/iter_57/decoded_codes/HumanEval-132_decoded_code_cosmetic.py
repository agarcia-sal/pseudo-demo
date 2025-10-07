from typing import List

def is_nested(text: str) -> bool:
    start_indices: List[int] = []
    end_indices: List[int] = []
    idx: int = 0
    length: int = len(text)
    while idx < length:
        if text[idx] == '[':
            start_indices.append(idx)
        else:
            end_indices.append(idx)
        idx += 1
    end_indices.reverse()
    matched_pairs: int = 0
    pos: int = 0
    max_pos: int = len(end_indices)
    for element in start_indices:
        if not (pos >= max_pos or element >= end_indices[pos]):
            matched_pairs += 1
            pos += 1
    return matched_pairs >= 2