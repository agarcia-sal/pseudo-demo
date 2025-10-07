from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total = 0
    for index in range(min(integer_k, len(array_of_integers))):
        current_value = array_of_integers[index]
        if len(str(abs(current_value))) <= 2:
            total += current_value
    return total