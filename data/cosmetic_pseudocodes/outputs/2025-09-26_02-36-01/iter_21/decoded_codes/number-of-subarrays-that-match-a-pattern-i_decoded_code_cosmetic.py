from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        count = 0
        i = 0
        while i <= n - m - 1:
            match = True
            for j in range(m):
                if pattern[j] == 1:
                    if not (nums[i + j + 1] > nums[i + j]):
                        match = False
                        break
                elif pattern[j] == 0:
                    if nums[i + j + 1] != nums[i + j]:
                        match = False
                        break
                elif pattern[j] == -1:
                    if not (nums[i + j + 1] < nums[i + j]):
                        match = False
                        break
            if match:
                count += 1
            i += 1
        return count