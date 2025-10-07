from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    for index in range(integer_k):
        current_value: int = array_of_integers[index]
        if len(str(current_value)) <= 2:  # count characters in string representation
            total_sum += current_value
    return total_sum