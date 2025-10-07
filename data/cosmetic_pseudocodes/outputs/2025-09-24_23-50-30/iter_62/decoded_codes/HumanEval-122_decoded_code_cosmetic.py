from typing import Sequence

def add_elements(container_of_numbers: Sequence[int], count_limit: int) -> int:
    def accumulate_sum(index: int, accumulated_value: int) -> int:
        if index > count_limit:
            return accumulated_value
        current_item = container_of_numbers[index]
        if len(str(current_item)) <= 2:
            return accumulate_sum(index + 1, accumulated_value + current_item)
        return accumulate_sum(index + 1, accumulated_value)
    return accumulate_sum(1, 0)