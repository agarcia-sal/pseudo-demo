from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    aggregated_total = 0
    count = 0
    while count < integer_k:
        current_value = array_of_integers[count]
        if len(str(current_value)) <= 2:
            aggregated_total += current_value
        count += 1
    return aggregated_total