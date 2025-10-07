from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        def compareAndIncrement(opCount: int, idx: int) -> int:
            if idx < 0:
                return opCount
            if nums[idx] > k:
                opCount += nums[idx] - k
                return compareAndIncrement(opCount, idx - 1)
            else:
                return opCount

        def compareAndIncrementForward(opCount: int, idx: int, limit: int) -> int:
            if idx >= limit:
                return opCount
            if nums[idx] < k:
                opCount += k - nums[idx]
                return compareAndIncrementForward(opCount, idx + 1, limit)
            else:
                return opCount

        lengthOfArray = len(nums)
        nums.sort()

        # Calculate midIdx according to pseudocode:
        # midIdx = (lengthOfArray / 2) - ( (lengthOfArray % 2) == 0 ? 1 : 0 ) + ((lengthOfArray % 2) == 0 ? 1 : 0)
        # Simplified: for even length: midIdx = lengthOfArray // 2
        #             for odd length: midIdx = lengthOfArray // 2
        # Actually, midIdx = lengthOfArray // 2 regardless
        # Confirming with the expression:
        # For lengthOfArray even:
        # midIdx = (lengthOfArray / 2) - 1 + 1 = lengthOfArray / 2
        # For odd:
        # midIdx = (lengthOfArray / 2) - 0 + 0 = lengthOfArray // 2
        # So midIdx = lengthOfArray // 2 in Python integer division

        midIdx = lengthOfArray // 2

        # If the median is already k, return 0
        if nums[midIdx] == k:
            return 0

        if nums[midIdx] < k:
            operationsCount = compareAndIncrementForward(0, midIdx, lengthOfArray)
        else:
            operationsCount = compareAndIncrement(0, midIdx)

        return operationsCount