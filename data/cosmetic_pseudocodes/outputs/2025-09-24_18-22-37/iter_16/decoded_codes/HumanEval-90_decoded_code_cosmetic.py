from typing import Sequence, Optional

def next_smallest(sequence_of_nums: Sequence[int]) -> Optional[int]:
    filtered_unique_nums: list[int] = []
    idx: int = 0
    while idx < len(sequence_of_nums):
        curr_item = sequence_of_nums[idx]
        if curr_item not in filtered_unique_nums:
            filtered_unique_nums.append(curr_item)
        idx += 1

    sorted_unique_nums: list[int] = []
    while filtered_unique_nums:
        min_val = filtered_unique_nums[0]
        pos = 0
        loop_i = 1
        while loop_i < len(filtered_unique_nums):
            if filtered_unique_nums[loop_i] < min_val:
                min_val = filtered_unique_nums[loop_i]
                pos = loop_i
            loop_i += 1
        sorted_unique_nums.append(min_val)
        filtered_unique_nums.pop(pos)

    if len(sorted_unique_nums) <= 1:
        return None

    return sorted_unique_nums[1]