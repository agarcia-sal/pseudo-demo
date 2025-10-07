from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    max_val: Optional[int] = None
    output_array: List[int] = []

    idx: int = 0
    while idx < len(list_of_numbers):
        current_num: int = list_of_numbers[idx]
        if max_val is None:
            max_val = current_num
        else:
            if current_num > max_val:
                max_val = current_num
        output_array.append(max_val)
        idx += 1

    return output_array