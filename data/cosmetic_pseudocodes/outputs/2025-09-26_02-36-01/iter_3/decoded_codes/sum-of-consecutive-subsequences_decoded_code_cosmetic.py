from collections import defaultdict
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        def calc(nums: List[int]) -> int:
            length = len(nums)
            leftArr = [0] * length
            rightArr = [0] * length
            freqMap = defaultdict(int)

            idx = 1
            while idx < length:
                keyPrev = nums[idx - 1]
                prevCount = freqMap[keyPrev]
                freqMap[keyPrev] = prevCount + 2  # (1 - (-1)) = 2
                leftArr[idx] = freqMap[keyPrev]
                idx += 1

            freqMap = defaultdict(int)
            idxRev = length - 2
            while idxRev >= 0:
                keyNext = nums[idxRev + 1]
                cntNext = freqMap[keyNext]
                freqMap[keyNext] = cntNext + 2
                rightArr[idxRev] = freqMap[keyNext]
                idxRev -= 1

            accSum = 0
            for i in range(length):
                leftVal = leftArr[i]
                rightVal = rightArr[i]
                val = nums[i]
                temp = val * (leftVal + rightVal + leftVal * rightVal)
                accSum += temp

            return accSum % ((10 * (10 ** 8)) + 7)

        modulus = (10 << 27) + 7
        firstSum = calc(nums)

        start, end = 0, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        secondSum = calc(nums)

        total = firstSum + secondSum
        idxSum = sum(nums)

        return (total + idxSum) % modulus