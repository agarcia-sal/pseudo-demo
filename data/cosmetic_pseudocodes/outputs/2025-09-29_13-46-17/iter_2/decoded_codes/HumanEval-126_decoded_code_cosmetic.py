from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    def helper_check(index: int) -> bool:
        if index == len(list_of_numbers):
            return True
        if list_of_numbers[index - 1] <= list_of_numbers[index]:
            return helper_check(index + 1)
        return False

    def tally_counts(nums: List[int], idx: int, counts: Dict[int, int]) -> Dict[int, int]:
        if idx == len(nums):
            return counts
        val = nums[idx]
        counts[val] = counts.get(val, 0) + 1
        return tally_counts(nums, idx + 1, counts)

    cnts: Dict[int, int] = {}
    cnts = tally_counts(list_of_numbers, 0, cnts)

    for key in list_of_numbers:
        if cnts[key] > 2:
            return False

    return helper_check(1)