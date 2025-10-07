from typing import List

def add_elements(data_list: List[int], limit: int) -> int:
    total_sum: int = 0
    counter: int = 0

    while counter < limit:
        current_value = data_list[counter]

        digit_count = len(str(current_value))
        if digit_count <= 2:
            total_sum += current_value

        counter += 1

    return total_sum