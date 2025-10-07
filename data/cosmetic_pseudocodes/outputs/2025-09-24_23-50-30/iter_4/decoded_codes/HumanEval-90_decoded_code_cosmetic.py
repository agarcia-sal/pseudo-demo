from typing import Iterable, Optional

def next_smallest(numbers: Iterable[int]) -> Optional[int]:
    unique_vals: dict[int, bool] = {}
    for val in numbers:
        unique_vals[val] = True
    unique_list = [key for key in unique_vals]
    unique_list.sort()
    return unique_list[1] if len(unique_list) > 1 else None