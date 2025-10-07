from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def helper_function(current_idx: int, max_idx: int, acc: List[int]) -> List[int]:
        if current_idx > max_idx:
            return acc
        new_value = positive_integer_n + (current_idx << 1)
        return helper_function(current_idx + 1, max_idx, acc + [new_value])
    return helper_function(0, positive_integer_n - 1, [])