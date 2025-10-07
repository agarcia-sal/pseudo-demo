from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    delta: int = 1

    for elem in array_of_integers:
        if elem == 0:
            delta = 0
            break

    if delta != 0:
        counter = 0
        for i in range(len(array_of_integers) - 1, -1, -1):
            if array_of_integers[i] < 0:
                counter += 1
        delta = 1 - 2 * (counter % 2)

    aggregate = 0
    idx = 0
    while idx < len(array_of_integers):
        val = array_of_integers[idx]
        aggregate += -val if val < 0 else val
        idx += 1

    return delta * aggregate