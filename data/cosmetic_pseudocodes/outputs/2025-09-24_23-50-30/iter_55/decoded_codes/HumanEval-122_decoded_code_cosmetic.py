from typing import List


def add_elements(list_numbers: List[int], count_limit: int) -> int:
    aggregate_sum: int = 0
    current_index: int = 0
    while current_index < count_limit:
        number_string: str = str(list_numbers[current_index])
        if len(number_string) <= 2:
            aggregate_sum += list_numbers[current_index]
        current_index += 1
    return aggregate_sum