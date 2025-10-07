from typing import List


def smallest_change(input_list: List[int]) -> int:
    def helper(i: int, count: int) -> int:
        if i >= len(input_list) // 2:
            return count
        return helper(i + 1, count + (1 if input_list[i] != input_list[len(input_list) - i - 1] else 0))

    return helper(0, 0)