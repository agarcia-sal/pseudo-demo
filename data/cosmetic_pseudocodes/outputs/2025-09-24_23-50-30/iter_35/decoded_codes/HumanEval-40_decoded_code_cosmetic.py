from typing import List

def triples_sum_to_zero(nums: List[int]) -> bool:
    lenNum: int = len(nums)
    p: int = 0
    while p < lenNum - 2:
        q: int = p + 1
        while q < lenNum - 1:
            r: int = q + 1
            while r < lenNum:
                if nums[p] + nums[q] + nums[r] == 0:
                    return True
                r += 1
            q += 1
        p += 1
    return False