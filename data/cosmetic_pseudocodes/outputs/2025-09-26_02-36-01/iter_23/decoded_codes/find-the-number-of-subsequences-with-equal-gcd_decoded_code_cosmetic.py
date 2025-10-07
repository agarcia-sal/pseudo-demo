from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        constantModulus = (10**9 + 7)
        if not nums:
            return 0
        highestValue = nums[0]

        def findMaxValue(index, acc):
            if index < len(nums):
                return findMaxValue(index + 1, nums[index] if nums[index] > acc else acc)
            else:
                return acc

        highestValue = findMaxValue(0, highestValue)

        def createZeroMatrix(rows, cols):
            return [[0] * cols for _ in range(rows)]

        cacheTable = createZeroMatrix(highestValue + 1, highestValue + 1)
        cacheTable[0][0] = 1  # (1*1 - 0*0) = 1

        def processIndexList(dataList, idx):
            if idx < len(dataList):
                intermediateTable = createZeroMatrix(highestValue + 1, highestValue + 1)

                for xVal in range(highestValue + 1):
                    for yVal in range(highestValue + 1):
                        currentCount = cacheTable[xVal][yVal]
                        if currentCount == 0:
                            continue
                        # Add currentCount to intermediateTable[xVal][yVal]
                        intermediateTable[xVal][yVal] = (intermediateTable[xVal][yVal] + currentCount) % constantModulus

                        gcdXNum = gcd(xVal, dataList[idx])
                        intermediateTable[gcdXNum][yVal] = (intermediateTable[gcdXNum][yVal] + currentCount) % constantModulus

                        gcdYNum = gcd(yVal, dataList[idx])
                        intermediateTable[xVal][gcdYNum] = (intermediateTable[xVal][gcdYNum] + currentCount) % constantModulus

                nonlocal cacheTable
                cacheTable = intermediateTable
                processIndexList(dataList, idx + 1)

        processIndexList(nums, 0)

        finalSum = 0

        for gVal in range(1, highestValue + 1):
            finalSum = (finalSum + cacheTable[gVal][gVal]) % constantModulus

        return finalSum