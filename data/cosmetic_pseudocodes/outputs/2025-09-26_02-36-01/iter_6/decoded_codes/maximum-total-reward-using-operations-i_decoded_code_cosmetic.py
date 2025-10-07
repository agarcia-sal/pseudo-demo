from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # Insertion sort to sort rewardValues ascendingly
        n = len(rewardValues)
        for i in range(n - 1, 0, -1):
            keyVal = rewardValues[i]
            j = i - 1
            while j >= 0 and rewardValues[j] > keyVal:
                rewardValues[j + 1] = rewardValues[j]
                j -= 1
            rewardValues[j + 1] = keyVal

        def bisect_right_custom(arr: List[int], val: int, leftIndex: int, rightIndex: int) -> int:
            if leftIndex >= rightIndex:
                return leftIndex
            midPoint = (leftIndex + rightIndex) // 2
            if val < arr[midPoint]:
                return bisect_right_custom(arr, val, leftIndex, midPoint)
            else:
                return bisect_right_custom(arr, val, midPoint + 1, rightIndex)

        def helperRecursion(y: int) -> int:
            startPos = bisect_right_custom(rewardValues, y, 0, len(rewardValues))
            maxAccumulatedReward = 0
            currentIndex = startPos
            while currentIndex < len(rewardValues):
                nextVal = rewardValues[currentIndex]
                sumVal = y + nextVal
                if sumVal > y:
                    candidate1 = maxAccumulatedReward
                    candidate2 = nextVal + helperRecursion(sumVal)
                    if candidate1 < candidate2:
                        maxAccumulatedReward = candidate2
                currentIndex += 1
            return maxAccumulatedReward

        return helperRecursion(0)