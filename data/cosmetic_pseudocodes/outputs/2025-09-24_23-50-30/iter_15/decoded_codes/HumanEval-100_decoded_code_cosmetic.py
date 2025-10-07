from typing import List

def make_a_pile(base_value: int) -> List[int]:
    accumulator: List[int] = []
    counter: int = 0

    while not (counter > base_value - 1):
        accumulator.append(base_value + (counter + counter))
        counter += 1

    return accumulator