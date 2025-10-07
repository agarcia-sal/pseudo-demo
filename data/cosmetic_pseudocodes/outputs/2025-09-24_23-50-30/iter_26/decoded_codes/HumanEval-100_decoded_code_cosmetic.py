from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    accumulator: List[int] = []
    pointer: int = 0

    while pointer < positive_integer_n:
        element: int = (pointer * 2) + positive_integer_n
        accumulator.append(element)
        pointer += 1

    return accumulator