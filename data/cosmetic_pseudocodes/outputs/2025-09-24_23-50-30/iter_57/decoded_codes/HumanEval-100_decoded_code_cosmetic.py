from typing import List

def make_a_pile(positive_integer_beta: int) -> List[int]:
    accumulator: List[int] = []
    iterator_counter: int = 0
    while iterator_counter < positive_integer_beta:
        temporary_value: int = (2 * iterator_counter) + positive_integer_beta
        accumulator.append(temporary_value)
        iterator_counter += 1
    return accumulator