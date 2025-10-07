from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    aggregated_total: int = 0
    processed_count: int = 0
    while processed_count < integer_k:
        current_value: int = array_of_integers[processed_count]
        if not (len(str(current_value)) > 2):
            aggregated_total += current_value
        processed_count += 1
    return aggregated_total