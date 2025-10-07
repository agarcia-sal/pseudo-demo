from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        lengthNums = len(nums)
        fMatrix = [[0] * (k + 1) for _ in range(lengthNums)]
        mpArray = [defaultdict(int) for _ in range(k + 1)]
        gArr = [[0, 0, 0] for _ in range(k + 1)]
        result = 0

        indexI = 0
        while indexI < lengthNums:
            currentValue = nums[indexI]
            hCounter = 0
            while hCounter <= k:
                fMatrix[indexI][hCounter] = mpArray[hCounter][currentValue]

                if hCounter != 0:
                    if gArr[hCounter - 1][0] != currentValue:
                        candidate1 = gArr[hCounter - 1][1]
                        if fMatrix[indexI][hCounter] < candidate1:
                            fMatrix[indexI][hCounter] = candidate1
                    else:
                        candidate2 = gArr[hCounter - 1][2]
                        if fMatrix[indexI][hCounter] < candidate2:
                            fMatrix[indexI][hCounter] = candidate2

                fMatrix[indexI][hCounter] += 1

                oldVal = mpArray[hCounter][currentValue]
                if oldVal < fMatrix[indexI][hCounter]:
                    mpArray[hCounter][currentValue] = fMatrix[indexI][hCounter]

                if gArr[hCounter][0] != currentValue:
                    if fMatrix[indexI][hCounter] >= gArr[hCounter][1]:
                        gArr[hCounter][2] = gArr[hCounter][1]
                        gArr[hCounter][1] = fMatrix[indexI][hCounter]
                        gArr[hCounter][0] = currentValue
                    else:
                        if gArr[hCounter][2] < fMatrix[indexI][hCounter]:
                            gArr[hCounter][2] = fMatrix[indexI][hCounter]
                else:
                    if gArr[hCounter][1] < fMatrix[indexI][hCounter]:
                        gArr[hCounter][1] = fMatrix[indexI][hCounter]

                if result < fMatrix[indexI][hCounter]:
                    result = fMatrix[indexI][hCounter]

                hCounter += 1

            indexI += 1

        return result