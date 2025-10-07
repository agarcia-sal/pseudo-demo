from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        t1 = len(nums)
        arr1 = [0] * t1
        q1 = t1 - 1
        while q1 >= 0:
            v1 = 0
            q2 = q1 + 1
            while q2 < t1:
                temp1 = (q2 - q1) * nums[q2]
                temp2 = temp1 + arr1[q2]
                if v1 < temp2:
                    v1 = temp2
                q2 += 1
            arr1[q1] = v1
            q1 -= 1
        return arr1[0]