from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0

    def process(index: int) -> int:
        nonlocal accumulator
        if not (index < integer_k):
            return accumulator
        current = array_of_integers[index]
        if len(str(current)) <= 2:
            accumulator += current
        return process(index + 1)

    return process(0)