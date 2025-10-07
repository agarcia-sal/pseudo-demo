from typing import List

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return nums[0]

        resultArray = [0] * length
        resultArray[length - 1] = nums[length - 1]

        def powerWithNegOne(exponent: int) -> int:
            return 1 if exponent % 2 == 0 else -1

        def traverseDescending(index: int) -> None:
            tempSum = nums[index]
            if tempSum > resultArray[index + 1]:
                resultArray[index] = tempSum
            else:
                resultArray[index] = resultArray[index + 1] + tempSum

            u = index + 1
            while u < length:
                powerDiff = u - index
                altSign = powerWithNegOne(powerDiff)
                tempSum += nums[u] * altSign

                if u + 1 < length:
                    candidate = tempSum + resultArray[u + 1]
                    if resultArray[index] < candidate:
                        resultArray[index] = candidate
                else:
                    if resultArray[index] < tempSum:
                        resultArray[index] = tempSum
                u += 1

        currentIndex = length - 2
        while currentIndex >= 0:
            traverseDescending(currentIndex)
            currentIndex -= 1

        return resultArray[0]