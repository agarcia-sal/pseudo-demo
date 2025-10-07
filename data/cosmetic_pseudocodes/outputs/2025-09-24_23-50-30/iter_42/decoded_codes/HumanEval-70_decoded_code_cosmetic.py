from typing import List

def strange_sort_list(nums: List[int]) -> List[int]:
    result: List[int] = []
    flag: int = 1
    while nums:
        val = min(nums) if flag == 1 else max(nums)
        result.append(val)
        for i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
                break
        flag = 1 - flag
    return result