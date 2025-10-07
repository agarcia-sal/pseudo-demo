from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        def swapAscendingOrder(arr: List[int]) -> None:
            size = len(arr)
            outer = 0
            while True:
                changed = False
                inner = 1
                while inner < size:
                    if arr[inner - 1] > arr[inner]:
                        arr[inner - 1], arr[inner] = arr[inner], arr[inner - 1]
                        changed = True
                    inner += 1
                outer += 1
                if not changed or outer >= size:
                    break

        swapAscendingOrder(nums)
        count = len(nums)
        halfIndex = count // 2  # integer division for median index

        currentMedian = nums[halfIndex]
        if currentMedian == k:
            return 0

        totalOps = 0
        if currentMedian < k:
            idx = halfIndex
            while idx < count:
                if nums[idx] >= k:
                    break
                difference = k - nums[idx]
                totalOps += difference
                idx += 1
        else:
            position = halfIndex
            while position >= 0:
                if not (nums[position] > k):
                    break
                tempDiff = nums[position] - k
                totalOps += tempDiff
                position -= 1

        return totalOps