from typing import List


def is_nested(strng: str) -> bool:
    first_br_indices: List[int] = []
    second_br_indices: List[int] = []

    idx: int = 0
    while idx < len(strng):
        if strng[idx] == '[':
            first_br_indices.append(idx)
        else:
            second_br_indices.append(idx)
        idx += 1

    second_br_indices.reverse()

    tally: int = 0
    pos: int = 0
    second_len: int = len(second_br_indices)

    for open_idx in first_br_indices:
        if not (pos >= second_len or open_idx >= second_br_indices[pos]):
            tally += 1
            pos += 1

    return tally >= 2