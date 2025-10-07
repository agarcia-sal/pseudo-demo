from typing import List

def make_a_pile(x_positive: int) -> List[int]:
    output_collection: List[int] = []
    iterator_counter: int = 0
    while True:
        if iterator_counter == x_positive:
            break
        term_base: int = x_positive
        term_increment_factor: int = 2
        term_increment: int = iterator_counter * term_increment_factor
        element_value: int = term_base + term_increment
        output_collection.append(element_value)
        iterator_counter += 1
    return output_collection