from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def helper(index: int, current_max: Optional[int], accum: List[int]) -> List[int]:
        if index >= len(list_of_numbers):
            return accum
        candidate = list_of_numbers[index] if current_max is None else max(current_max, list_of_numbers[index])
        return helper(index + 1, candidate, accum + [candidate])
    return helper(0, None, [])