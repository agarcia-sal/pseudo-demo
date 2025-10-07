from typing import List

def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    idx: int = 0
    length: int = len(string)
    while idx < length:
        current_char: str = string[idx]
        if current_char == '[':
            open_indices.append(idx)
        else:
            close_indices.append(idx)
        idx += 1

    close_indices.reverse()

    matches: int = 0
    pos_ptr: int = 0
    close_len: int = len(close_indices)

    i: int = 0
    open_len: int = len(open_indices)
    while i < open_len:
        open_idx: int = open_indices[i]
        if pos_ptr < close_len and open_idx < close_indices[pos_ptr]:
            matches += 1
            pos_ptr += 1
        i += 1

    return matches >= 2