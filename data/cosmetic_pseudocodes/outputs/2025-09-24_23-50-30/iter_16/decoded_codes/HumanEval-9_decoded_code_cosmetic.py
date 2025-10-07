from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def recur(idx: int, curr_max: Optional[int], accum: List[int]) -> List[int]:
        if idx == len(list_of_numbers):
            return accum
        current_value = list_of_numbers[idx]
        updated_max = current_value if curr_max is None or current_value > curr_max else curr_max
        return recur(idx + 1, updated_max, accum + [updated_max])

    return recur(0, None, [])