from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)  # Rearrange so each next element is <= preceding
        totalHappiness = 0
        reductionFactor = 0
        counter = 0
        while counter < k:
            valueAtCurrentPosition = happiness[counter] - reductionFactor
            if valueAtCurrentPosition < 0:
                valueAtCurrentPosition = 0
            totalHappiness += valueAtCurrentPosition
            reductionFactor += 1
            counter += 1
        return totalHappiness