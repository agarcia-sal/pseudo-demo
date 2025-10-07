from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    accumulator: List[int] = []
    cursor: int = 0

    while cursor < positive_integer_n:
        current_element: int = cursor * 2 + positive_integer_n
        accumulator.append(current_element)
        cursor += 1

    return accumulator