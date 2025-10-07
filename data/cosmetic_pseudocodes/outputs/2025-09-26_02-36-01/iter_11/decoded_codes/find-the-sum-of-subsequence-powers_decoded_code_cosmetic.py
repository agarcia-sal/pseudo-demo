from itertools import combinations
from typing import List

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        def CalculateAbsDifference(x: int, y: int) -> int:
            if x >= y:
                return x - y
            else:
                return y - x

        modValue = 10**9 + 7
        accumulator = 0
        comboList = list(combinations(nums, k))

        def AccumulateMinDiff(comb: List[int], posA: int, posB: int, currMin: int) -> int:
            if posA >= len(comb):
                return currMin
            else:
                if posB >= len(comb):
                    return AccumulateMinDiff(comb, posA + 1, posA + 2, currMin)
                diffValue = CalculateAbsDifference(comb[posA], comb[posB])
                newMin = currMin
                if diffValue < currMin:
                    newMin = diffValue
                return AccumulateMinDiff(comb, posA, posB + 1, newMin)

        def ProcessComboList(index: int) -> None:
            nonlocal accumulator
            if index >= len(comboList):
                return
            currentCombo = comboList[index]
            infinityEquivalent = 999999999999
            minimumDiff = AccumulateMinDiff(currentCombo, 0, 1, infinityEquivalent)
            accumulator += minimumDiff
            accumulator %= modValue
            ProcessComboList(index + 1)

        ProcessComboList(0)
        return accumulator