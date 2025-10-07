from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def determine_relation(a: int, b: int) -> int:
            if not (a >= b):
                return 1
            else:
                if a == b:
                    return 0
                else:
                    return -1

        w = len(nums)
        v = len(pattern)

        x = []
        for y in range(w - 1):
            x.append(determine_relation(nums[y], nums[y + 1]))

        count = 0
        z = 0
        while z <= w - v - 1:
            s = True
            for t in range(v):
                if x[z + t] != pattern[t]:
                    s = False
                    break
            if s:
                count += 1
            z += 1

        return count