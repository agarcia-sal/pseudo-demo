from typing import List


def add_elements(list_of_numbers: List[int], count_limit: int) -> int:
    aggregate_total = 0
    index_marker = 0
    while index_marker < count_limit:
        current_value = list_of_numbers[index_marker]
        if len(str(current_value)) <= 2:
            aggregate_total += current_value
        index_marker += 1
    return aggregate_total