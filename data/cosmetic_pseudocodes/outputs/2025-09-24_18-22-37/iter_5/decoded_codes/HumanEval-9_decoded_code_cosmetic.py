from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    idx: int = 0
    result_list: List[int] = []
    current_max: Optional[int] = None

    while idx < len(list_of_numbers):
        candidate: int = list_of_numbers[idx]
        idx += 1

        if current_max is None:
            current_max = candidate
        else:
            if candidate > current_max:
                current_max = candidate

        result_list.append(current_max)

    return result_list