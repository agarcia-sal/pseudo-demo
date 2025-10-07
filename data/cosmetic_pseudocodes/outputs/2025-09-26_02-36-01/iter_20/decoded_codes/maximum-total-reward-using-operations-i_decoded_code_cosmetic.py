from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:

        def binarySearchRight(target: int, arr: List[int]) -> int:
            start, end = 0, len(arr)
            while start < end:
                mid = (start + end) // 2
                if arr[mid] <= target:
                    start = mid + 1
                else:
                    end = mid
            return start

        def computeDepth(flag: int) -> int:
            idx = binarySearchRight(flag, rewardValues)
            cumulativeMax = 0
            counter = idx
            while counter < len(rewardValues):
                currentVal = rewardValues[counter]
                if (flag + currentVal) > flag:
                    candidate = currentVal + computeDepth(flag + currentVal)
                    if candidate > cumulativeMax:
                        cumulativeMax = candidate
                counter += 1
            return cumulativeMax

        def quickSortAsc(array: List[int], left: int, right: int) -> None:
            if left >= right:
                return
            pivot = array[right]
            i = left - 1
            j = left
            while j < right:
                if array[j] < pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
                j += 1
            array[i + 1], array[right] = array[right], array[i + 1]
            quickSortAsc(array, left, i)
            quickSortAsc(array, i + 2, right)

        quickSortAsc(rewardValues, 0, len(rewardValues) - 1)
        return computeDepth(0)