from typing import List

def make_a_pile(almost_positive_x: int) -> List[int]:
    result_stack: List[int] = []
    iterator_counter: int = 0

    while iterator_counter < almost_positive_x:
        intermediate_v = (2 * iterator_counter) + almost_positive_x
        result_stack.append(intermediate_v)
        iterator_counter += 1

    return result_stack