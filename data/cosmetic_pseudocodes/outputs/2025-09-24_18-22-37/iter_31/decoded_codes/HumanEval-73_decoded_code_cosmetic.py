from typing import Sequence

def smallest_change(collection_of_numbers: Sequence[int]) -> int:
    result_counter: int = 0
    position: int = 0
    n: int = len(collection_of_numbers)
    limit: int = (n // 2)  # integer division to handle lengths correctly
    while position < limit:
        forward_element = collection_of_numbers[position]
        backward_pos = n - position - 1
        backward_element = collection_of_numbers[backward_pos]
        if forward_element != backward_element:
            result_counter += 1
        position += 1
    return result_counter