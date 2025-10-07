from typing import List


def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    idx: int = 0

    while idx < len(string):
        if string[idx] == '[':
            open_indices.append(idx)
        else:
            close_indices.append(idx)
        idx += 1

    close_indices.reverse()

    match_count: int = 0
    pointer: int = 0
    total_close: int = len(close_indices)

    for element in open_indices:
        if pointer < total_close and element < close_indices[pointer]:
            match_count += 1
            pointer += 1

    return match_count >= 2