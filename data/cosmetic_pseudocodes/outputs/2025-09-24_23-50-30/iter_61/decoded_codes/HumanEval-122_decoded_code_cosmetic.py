from typing import List

def add_elements(list_of_ints: List[int], num: int) -> int:
    def helper(idx: int, acc: int) -> int:
        if idx >= num:
            return acc
        if len(str(list_of_ints[idx])) > 2:
            return helper(idx + 1, acc)
        return helper(idx + 1, acc + list_of_ints[idx])
    return helper(0, 0)