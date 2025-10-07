from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        lengthVal = len(nums)
        fMatrix = [[0] * lengthVal for _ in range(lengthVal)]
        gMatrix = [[0] * lengthVal for _ in range(lengthVal)]

        idx = lengthVal - 1
        while idx >= 0:
            fMatrix[idx][idx] = nums[idx]
            gMatrix[idx][idx] = nums[idx]
            nextIdx = idx + 1
            while nextIdx < lengthVal:
                fMatrix[idx][nextIdx] = fMatrix[idx][nextIdx - 1] ^ fMatrix[idx + 1][nextIdx]
                temp1 = gMatrix[idx][nextIdx - 1]
                temp2 = gMatrix[idx + 1][nextIdx]
                temp3 = fMatrix[idx][nextIdx]
                max_val = temp3
                if temp1 > max_val:
                    max_val = temp1
                if temp2 > max_val:
                    max_val = temp2
                gMatrix[idx][nextIdx] = max_val
                nextIdx += 1
            idx -= 1

        resultList = []
        for leftPos, rightPos in queries:
            resultList.append(gMatrix[leftPos][rightPos])

        return resultList