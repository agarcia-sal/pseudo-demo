class Solution:
    def subsequencePairCount(self, nums):
        M = 10**9 + 7

        def computeGCD(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        maxElement = 0
        for num in nums:
            if num > maxElement:
                maxElement = num

        countsMatrix = [[0] * (maxElement + 1) for _ in range(maxElement + 1)]
        countsMatrix[0][0] = 1

        def updateCounts(currentCounts, currentNumber):
            updatedCounts = [[0] * (maxElement + 1) for _ in range(maxElement + 1)]

            for outerIdx in range(maxElement + 1):
                for innerIdx in range(maxElement + 1):
                    val = currentCounts[outerIdx][innerIdx]
                    if val == 0:
                        continue

                    updatedCounts[outerIdx][innerIdx] = (updatedCounts[outerIdx][innerIdx] + val) % M

                    gcdWithNum1 = computeGCD(outerIdx, currentNumber)
                    updatedCounts[gcdWithNum1][innerIdx] = (updatedCounts[gcdWithNum1][innerIdx] + val) % M

                    gcdWithNum2 = computeGCD(innerIdx, currentNumber)
                    updatedCounts[outerIdx][gcdWithNum2] = (updatedCounts[outerIdx][gcdWithNum2] + val) % M

            return updatedCounts

        for num in nums:
            countsMatrix = updateCounts(countsMatrix, num)

        finalSum = 0
        for counter in range(1, maxElement + 1):
            finalSum += countsMatrix[counter][counter]

        finalSum %= M
        return finalSum