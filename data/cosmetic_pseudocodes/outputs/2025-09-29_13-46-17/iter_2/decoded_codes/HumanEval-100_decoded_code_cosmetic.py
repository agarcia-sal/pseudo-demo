from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def helper(current_index: int, acc: List[int]) -> List[int]:
        if not (current_index < positive_integer_n):
            return acc
        new_value = current_index * 2 + positive_integer_n
        return helper(current_index + 1, acc + [new_value])

    return helper(0, [])