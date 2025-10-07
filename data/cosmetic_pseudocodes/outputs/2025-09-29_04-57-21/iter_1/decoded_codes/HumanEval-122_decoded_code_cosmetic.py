from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    index: int = 0
    limit: int = min(integer_k, len(array_of_integers))  # Handle case if integer_k > len(array_of_integers)
    while index < limit:
        current = array_of_integers[index]
        if len(str(current)) <= 2:
            total_sum += current
        index += 1
    return total_sum