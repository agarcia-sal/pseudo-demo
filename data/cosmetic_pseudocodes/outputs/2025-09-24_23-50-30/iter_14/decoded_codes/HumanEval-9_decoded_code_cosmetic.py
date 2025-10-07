from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulative_max: Optional[int] = None
    output_collection: List[int] = []

    idx: int = 0
    while idx < len(list_of_numbers):
        current_val: int = list_of_numbers[idx]

        if accumulative_max is None:
            accumulative_max = current_val
        elif current_val > accumulative_max:
            accumulative_max = current_val

        output_collection.append(accumulative_max)
        idx += 1

    return output_collection