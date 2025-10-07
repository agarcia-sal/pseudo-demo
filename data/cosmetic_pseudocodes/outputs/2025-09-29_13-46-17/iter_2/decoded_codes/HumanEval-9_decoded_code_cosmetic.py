from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def helper(index: int, current_max: Optional[int]) -> List[int]:
        if index == len(list_of_numbers):
            return []
        num = list_of_numbers[index]
        new_max = num if current_max is None or num > current_max else current_max
        rest = helper(index + 1, new_max)
        return [new_max] + rest

    return helper(0, None)