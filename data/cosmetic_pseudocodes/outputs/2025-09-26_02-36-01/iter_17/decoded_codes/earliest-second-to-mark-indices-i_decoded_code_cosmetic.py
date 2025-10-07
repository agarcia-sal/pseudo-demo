from typing import List, Set

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        lengthNums = len(nums)
        lengthChanges = len(changeIndices)

        def can_mark_by_second(k: int) -> bool:
            occurrences = [-1] * lengthNums
            for idxCounter in range(k):
                pos = changeIndices[idxCounter] - 1
                occurrences[pos] = idxCounter

            totalNeeded = sum(nums)

            available = 0
            marked: Set[int] = set()

            step = 0
            while step < k:
                currentIndex = changeIndices[step] - 1
                if currentIndex not in marked:
                    if occurrences[currentIndex] == step:
                        if nums[currentIndex] <= available:
                            available -= nums[currentIndex]
                            marked.add(currentIndex)
                        else:
                            return False
                    else:
                        available += 1
                else:
                    available += 1
                step += 1

            return len(marked) == lengthNums

        lowerBound = 0
        upperBound = lengthChanges + 1

        while lowerBound < upperBound:
            midpoint = (lowerBound + upperBound) // 2
            if can_mark_by_second(midpoint):
                upperBound = midpoint
            else:
                lowerBound = midpoint + 1

        return lowerBound if lowerBound <= lengthChanges else -1