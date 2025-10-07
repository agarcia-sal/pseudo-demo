from typing import Sequence

def exchange(collection_a: Sequence[int], collection_b: Sequence[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    iterator_a: int = 0
    while iterator_a < len(collection_a):
        current_value: int = collection_a[iterator_a]
        if current_value % 2 != 0:
            tally_odd += 1
        iterator_a += 1

    iterator_b: int = 0
    while iterator_b < len(collection_b):
        current_element: int = collection_b[iterator_b]
        if (current_element % 2) == 0:
            tally_even += 1
        iterator_b += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"