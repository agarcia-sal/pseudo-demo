from typing import List

def minSubArraySum(array_of_nums: List[int]) -> int:
    acc: int = 0
    high_water: int = 0
    idx: int = 1

    while idx <= len(array_of_nums):
        curr_val: int = array_of_nums[idx - 1]
        neg_curr: int = -curr_val
        acc += neg_curr

        if acc < 0:
            acc = 0
        if acc > high_water:
            high_water = acc
        idx += 1

    if high_water == 0:
        negate_elements: List[int] = []
        pos: int = 1
        while pos <= len(array_of_nums):
            negate_elements.append(-array_of_nums[pos - 1])
            pos += 1

        high_water = negate_elements[0]
        for ele in negate_elements:
            if ele > high_water:
                high_water = ele

    result: int = -high_water
    return result