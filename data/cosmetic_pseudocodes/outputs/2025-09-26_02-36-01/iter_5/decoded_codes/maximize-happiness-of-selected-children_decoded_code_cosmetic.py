from typing import List

class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        self.sortDescending(happiness)

        def sumHelper(position: int, acc: int, dec: int) -> int:
            if position >= k:
                return acc
            tempVal = happiness[position] - dec
            if tempVal < 0:
                tempVal = 0
            return sumHelper(position + 1, acc + tempVal, dec + 1)

        cumulativeResult = sumHelper(0, 0, 0)
        return cumulativeResult

    def sortDescending(self, collection: List[int]) -> None:
        collection.sort(reverse=True)