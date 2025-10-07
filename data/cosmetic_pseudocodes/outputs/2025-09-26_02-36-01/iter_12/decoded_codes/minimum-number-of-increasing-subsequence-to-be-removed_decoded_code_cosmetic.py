from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def computeLength(arr: List[int]) -> int:
            if len(arr) == 0:
                return 0

            dp_arr = [1] * len(arr)

            def innerHelper(k: int, limit: int, acc: int) -> int:
                if k > limit:
                    return acc
                else:

                    def innerLoop(m: int, bound: int, currentMax: int) -> int:
                        if m > bound:
                            return currentMax
                        else:
                            if arr[k] <= arr[m]:
                                updatedMax = currentMax
                                if dp_arr[k] < dp_arr[m] + 1:
                                    updatedMax = dp_arr[m] + 1
                                dp_arr[k] = updatedMax
                                return innerLoop(m + 1, bound, updatedMax)
                            else:
                                return innerLoop(m + 1, bound, currentMax)

                    innerLoop(0, k - 1, 1)
                    return innerHelper(k + 1, limit, acc)

            innerHelper(1, len(arr) - 1, 1)

            def findMaxValue(array: List[int], index: int, limit: int, currentMax: int) -> int:
                if index > limit:
                    return currentMax
                else:
                    candidate = array[index]
                    if candidate > currentMax:
                        currentMax = candidate
                    return findMaxValue(array, index + 1, limit, currentMax)

            return findMaxValue(dp_arr, 0, len(dp_arr) - 1, dp_arr[0])

        return computeLength(nums)