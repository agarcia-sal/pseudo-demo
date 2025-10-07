from collections import defaultdict

class Solution:
    def getSum(self, nums):
        mod = 10**9 + 7

        def calc(arr):
            length = len(arr)
            leftArr = [0] * length
            rightArr = [0] * length
            countMap = defaultdict(int)

            for index in range(1, length):
                prevVal = arr[index - 1]
                incrementValue = 1 + countMap[prevVal - 1]
                countMap[prevVal] += incrementValue
                leftArr[index] = countMap[prevVal]

            countMap = defaultdict(int)

            for index in range(length - 2, -1, -1):
                nextVal = arr[index + 1]
                incrementValue = 1 + countMap[nextVal + 1]
                countMap[nextVal] += incrementValue
                rightArr[index] = countMap[nextVal]

            result = 0
            for i in range(length):
                lVal = leftArr[i]
                rVal = rightArr[i]
                elem = arr[i]
                result += (lVal + rVal + lVal * rVal) * elem

            return result % mod

        originalCalcResult = calc(nums)
        nums.reverse()
        reversedCalcResult = calc(nums)

        return (originalCalcResult + reversedCalcResult + sum(nums)) % mod