from collections import Counter
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        MOD_VALUE = 10**9 + 7

        def calc(array: List[int]) -> int:
            length = len(array)
            countsLeft = [0] * length
            countsRight = [0] * length
            histogram = Counter()

            # Calculate countsLeft
            for index in range(1, length):
                keyLeft = array[index - 1]
                newCountLeft = 1 + histogram[keyLeft - 1]
                histogram[keyLeft - 1] = newCountLeft
                countsLeft[index] = newCountLeft

            histogram = Counter()
            # Calculate countsRight
            for pointer in range(length - 2, -1, -1):
                keyRight = array[pointer + 1]
                newCountRight = 1 + histogram[keyRight + 1]
                histogram[keyRight + 1] = newCountRight
                countsRight[pointer] = newCountRight

            accumulator = 0
            for pos in range(length):
                valL = countsLeft[pos]
                valR = countsRight[pos]
                valX = array[pos]
                partialSum = (valL + valR + valL * valR) * valX
                accumulator += partialSum

            return accumulator % MOD_VALUE

        firstCalc = calc(nums)

        # Reverse nums in place
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        secondCalc = calc(nums)

        total = (firstCalc + secondCalc + sum(nums)) % MOD_VALUE
        return total