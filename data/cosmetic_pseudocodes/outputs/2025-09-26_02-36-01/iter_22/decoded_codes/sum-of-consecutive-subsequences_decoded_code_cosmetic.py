from collections import Counter

class Solution:
    def getSum(self, nums):
        mod = 10**9 + 7

        def calc(nums):
            size = len(nums)
            firstList = [0] * size
            secondList = [0] * size

            firstCounter = Counter()
            idx1 = 1
            while idx1 < size:
                val1 = nums[idx1 - 1]
                prevCount1 = firstCounter.get(val1, 0)
                firstCounter[val1] = prevCount1 + 1
                firstList[idx1] = firstCounter[val1]
                idx1 += 1

            secondCounter = Counter()
            idx2 = size - 2
            while idx2 >= 0:
                val2 = nums[idx2 + 1]
                prevCount2 = secondCounter.get(val2, 0)
                secondCounter[val2] = prevCount2 + 1
                secondList[idx2] = secondCounter[val2]
                idx2 -= 1

            accumulator = 0
            pos = 0
            while pos < size:
                leftVal = firstList[pos]
                rightVal = secondList[pos]
                currentVal = nums[pos]
                partialSum = (leftVal + rightVal + (leftVal * rightVal)) * currentVal
                accumulator += partialSum
                pos += 1

            return accumulator % mod

        resultX = calc(nums)
        reversedNums = nums[::-1]
        resultY = calc(reversedNums)
        sumAll = sum(nums)

        return (resultX + resultY + sumAll) % mod