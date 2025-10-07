from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def countRec(startIndex: int, total: int) -> int:
            if startIndex > len(nums) - 1:
                return total
            else:
                def innerCount(currentIndex: int, runningAnd: int, localCount: int) -> int:
                    if currentIndex > len(nums) - 1 or runningAnd < k:
                        return localCount
                    else:
                        newRunningAnd = runningAnd & nums[currentIndex]
                        updatedLocalCount = localCount + (1 if newRunningAnd == k else 0)
                        return innerCount(currentIndex + 1, newRunningAnd, updatedLocalCount)

                startAnd = nums[startIndex]
                innerResult = innerCount(startIndex, startAnd, 0)
                return countRec(startIndex + 1, total + innerResult)

        return countRec(0, 0)