from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    for index in range(integer_k):
        current_number: int = array_of_integers[index]
        if len(str(current_number)) <= 2:
            total_sum += current_number
    return total_sum