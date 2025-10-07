from typing import List

def smallest_change(list_of_ints: List[int]) -> int:
    def helper(pair_index: int, acc: int) -> int:
        if pair_index >= len(list_of_ints) // 2:
            return acc
        left_val = list_of_ints[pair_index]
        right_val = list_of_ints[len(list_of_ints) - 1 - pair_index]
        if left_val == right_val:
            return helper(pair_index + 1, acc)
        else:
            return helper(pair_index + 1, acc + 1)
    return helper(0, 0)