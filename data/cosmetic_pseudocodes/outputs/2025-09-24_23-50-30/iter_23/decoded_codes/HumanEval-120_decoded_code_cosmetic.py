from typing import List

def maximum(collection_of_nums: List[int], param_n: int) -> List[int]:
    if param_n != 0:
        ordered_nums = sorted(collection_of_nums)
        return ordered_nums[-param_n:] if param_n <= len(ordered_nums) else ordered_nums[:]
    return []