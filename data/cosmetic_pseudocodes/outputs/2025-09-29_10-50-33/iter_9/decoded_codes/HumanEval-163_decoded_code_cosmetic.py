from typing import List


def generate_integers(integer_a: int, integer_b: int) -> List[int]:
    threshold_minimum: int = 2 if 2 > min(integer_a, integer_b) else min(integer_a, integer_b)
    threshold_maximum: int = 8 if 8 < max(integer_a, integer_b) else max(integer_a, integer_b)
    collection_even: List[int] = []
    iterator_marker: int = threshold_minimum

    while not (iterator_marker > threshold_maximum):
        if iterator_marker % 2 == 0:
            collection_even.append(iterator_marker)
        iterator_marker += 1

    return collection_even