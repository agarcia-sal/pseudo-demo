from typing import List, Optional

def rolling_max(input_sequence: List[int]) -> List[int]:
    def helper(index: int, current_max: Optional[int], acc: List[int]) -> List[int]:
        if index == len(input_sequence):
            return acc
        next_val = input_sequence[index]
        updated_max = current_max if (current_max is not None and current_max >= next_val) else next_val
        return helper(index + 1, updated_max, acc + [updated_max])
    return helper(0, None, [])