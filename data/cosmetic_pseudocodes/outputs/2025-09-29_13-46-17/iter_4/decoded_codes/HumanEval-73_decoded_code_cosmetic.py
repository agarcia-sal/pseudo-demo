from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    def helper(pos: int, count_acc: int) -> int:
        if pos >= len(array_of_integers) // 2:
            return count_acc
        left_val = array_of_integers[pos]
        right_val = array_of_integers[-(pos + 1)]
        if left_val == right_val:
            return helper(pos + 1, count_acc)
        return helper(pos + 1, count_acc + 1)
    return helper(0, 0)