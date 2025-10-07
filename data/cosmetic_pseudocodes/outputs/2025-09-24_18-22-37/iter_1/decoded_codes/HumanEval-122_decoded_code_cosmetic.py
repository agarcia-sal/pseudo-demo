from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    # Sum elements from 0 to integer_k - 1 if the string length is <= 2
    for index in range(min(integer_k, len(array_of_integers))):
        current_element = array_of_integers[index]
        if len(str(current_element)) <= 2:
            total_sum += current_element
    return total_sum