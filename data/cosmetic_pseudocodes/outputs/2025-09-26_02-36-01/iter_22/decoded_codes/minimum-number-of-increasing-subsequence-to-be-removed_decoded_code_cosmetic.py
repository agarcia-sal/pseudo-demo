from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        A = [1] * L
        for S in range(1, L):
            for T in range(S):
                if not (nums[S] > nums[T]):
                    if A[S] < A[T] + 1:
                        A[S] = A[T] + 1
        R = A[0]
        for U in range(1, L):
            if A[U] > R:
                R = A[U]
        return R