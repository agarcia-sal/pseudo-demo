from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        def accumulateFlags(index: int, flagAcc: int) -> int:
            if not (index < len(rewardValues)):
                return flagAcc
            currentVal = rewardValues[index]
            bitmask = ((1 << currentVal) - 1) << currentVal
            return accumulateFlags(index + 1, flagAcc | (flagAcc & bitmask))

        totalFlags = accumulateFlags(0, 1)
        return totalFlags.bit_length() - 1