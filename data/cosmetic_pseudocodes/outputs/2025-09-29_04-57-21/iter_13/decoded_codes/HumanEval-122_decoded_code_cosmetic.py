from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    cumulative_total: int = 0

    def process_elements(index: int) -> None:
        nonlocal cumulative_total
        if index > integer_k:
            return
        current_value = array_of_integers[index]
        if not (len(str(current_value)) > 2):
            cumulative_total += current_value
        process_elements(index + 1)

    process_elements(1)
    return cumulative_total