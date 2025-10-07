from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def bitwiseAnd(a: int, b: int) -> int:
            return a & b

        A = len(nums)
        B = 0
        C = 0

        while C < A:
            D = nums[C]
            E = C
            while True:
                D = bitwiseAnd(D, nums[E])
                if D == k:
                    B += 1
                if D < k:
                    break
                E += 1
                if E >= A:
                    break
            C += 1
        return B