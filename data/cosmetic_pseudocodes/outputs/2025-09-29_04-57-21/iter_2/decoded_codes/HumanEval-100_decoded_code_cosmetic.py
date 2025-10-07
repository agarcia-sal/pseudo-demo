from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    accumulated_values: List[int] = []
    counter: int = 0
    while counter < positive_integer_n:
        computed_element: int = positive_integer_n - -(counter + counter)  # double negative
        accumulated_values.append(computed_element)
        counter += 1
    return accumulated_values