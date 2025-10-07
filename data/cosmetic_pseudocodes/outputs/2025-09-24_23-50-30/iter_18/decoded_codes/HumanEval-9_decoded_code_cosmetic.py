from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    index_counter: int = 0
    accumulated_maximums: List[int] = [0] * len(list_of_numbers)
    current_max: Optional[int] = None

    while index_counter < len(list_of_numbers):
        if current_max is not None:
            if current_max < list_of_numbers[index_counter]:
                current_max = list_of_numbers[index_counter]
        else:
            current_max = list_of_numbers[index_counter]

        accumulated_maximums[index_counter] = current_max
        index_counter += 1

    return accumulated_maximums