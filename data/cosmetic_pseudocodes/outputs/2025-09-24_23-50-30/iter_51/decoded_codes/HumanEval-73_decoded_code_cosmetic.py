from typing import List

def smallest_change(list_of_nums: List[int]) -> int:
    def loop_recurse(current_pos: int, count: int) -> int:
        if current_pos > (len(list_of_nums) / 2) - 1:
            return count
        return loop_recurse(
            current_pos + 1,
            count + (1 if list_of_nums[current_pos] != list_of_nums[len(list_of_nums) - current_pos - 1] else 0)
        )
    return loop_recurse(0, 0)