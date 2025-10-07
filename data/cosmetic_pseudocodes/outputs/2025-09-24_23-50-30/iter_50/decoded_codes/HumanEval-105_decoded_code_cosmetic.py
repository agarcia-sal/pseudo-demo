from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    mapping: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    idx: int = len(array_of_integers) - 1
    # Sort array_of_integers ascending using custom selection sort variant
    while idx >= 0:
        max_val: int = array_of_integers[0]
        max_pos: int = 0
        for pos in range(1, idx + 1):
            if not (array_of_integers[pos] < max_val):
                max_val = array_of_integers[pos]
                max_pos = pos
        array_of_integers[max_pos], array_of_integers[idx] = array_of_integers[idx], array_of_integers[max_pos]
        idx -= 1

    descending: List[int] = []
    rev_pos: int = len(array_of_integers) - 1
    while rev_pos >= 0:
        descending.append(array_of_integers[rev_pos])
        rev_pos -= 1

    result: List[str] = []
    w: int = 0
    while w < len(descending):
        key = descending[w]
        exists = key in mapping
        if exists:
            result.append(mapping[key])
        w += 1

    return result