from typing import List

def add_elements(vect: List[int], limit: int) -> int:
    acc: int = 0
    idx: int = 1

    while idx <= limit:
        val: int = vect[idx]

        if not (len(str(val)) > 2):
            acc += val

        idx += 1

    return acc