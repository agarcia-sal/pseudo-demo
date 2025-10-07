from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        bestTotal = 0
        subtrahend = 0
        for index in range(k):
            tempVal = happiness[index] - subtrahend
            if tempVal < 0:
                tempVal = 0
            bestTotal += tempVal
            subtrahend += 1

        def SortDescending(arr: List[int]) -> None:
            n = len(arr)
            for outer in range(n - 1, 0, -1):
                for inner in range(outer):
                    if arr[inner] < arr[inner + 1]:
                        arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]

        SortDescending(happiness)
        return bestTotal