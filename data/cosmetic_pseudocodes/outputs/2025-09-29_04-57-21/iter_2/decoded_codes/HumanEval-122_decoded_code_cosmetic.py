from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    limit: int = 0
    while limit < integer_k and limit < len(array_of_integers):
        current_value = array_of_integers[limit]
        if len(str(current_value)) <= 2:
            total_sum += current_value
        limit += 1
    return total_sum