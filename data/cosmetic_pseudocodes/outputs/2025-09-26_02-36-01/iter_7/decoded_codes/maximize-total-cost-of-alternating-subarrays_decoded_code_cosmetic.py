class Solution:
    def maximumTotalCost(self, nums):
        lengthVar = len(nums)
        if lengthVar == 1:
            return nums[0]
        else:
            dpArray = [0] * lengthVar
            dpArray[lengthVar - 1] = nums[lengthVar - 1]

            outerIdx = lengthVar - 2
            while outerIdx >= 0:
                sumTracker = nums[outerIdx]

                if sumTracker > dpArray[outerIdx + 1]:
                    dpArray[outerIdx] = sumTracker
                else:
                    dpArray[outerIdx] = dpArray[outerIdx + 1] + sumTracker

                innerCounter = outerIdx + 1
                while innerCounter < lengthVar:
                    signFactor = (-1) ** (innerCounter - outerIdx)
                    sumTracker += nums[innerCounter] * signFactor

                    if innerCounter + 1 < lengthVar:
                        if dpArray[outerIdx] < sumTracker + dpArray[innerCounter + 1]:
                            dpArray[outerIdx] = sumTracker + dpArray[innerCounter + 1]
                    else:
                        if dpArray[outerIdx] < sumTracker:
                            dpArray[outerIdx] = sumTracker

                    innerCounter += 1

                outerIdx -= 1

            return dpArray[0]