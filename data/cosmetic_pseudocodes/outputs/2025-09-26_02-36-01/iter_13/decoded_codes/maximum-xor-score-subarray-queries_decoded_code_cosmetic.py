class Solution:
    def maximumSubarrayXor(self, nums, queries):
        # Helper function to find length of list
        def lengthOfList(L):
            count = 0
            while True:
                try:
                    L[count]
                except IndexError:
                    break
                count += 1
            return count

        totalCount = lengthOfList(nums)

        # Generate rows x cols zero matrix
        def generateZeroMatrix(rows, cols):
            resultMatrix = []
            outerIdx = 0
            while True:
                if outerIdx == rows:
                    break
                innerList = []
                innerIdx = 0
                while True:
                    if innerIdx == cols:
                        break
                    innerList.append(0)
                    innerIdx += 1
                resultMatrix.append(innerList)
                outerIdx += 1
            return resultMatrix

        matrixA = generateZeroMatrix(totalCount, totalCount)
        matrixB = generateZeroMatrix(totalCount, totalCount)

        def maximum(x, y):
            return x if x >= y else y

        def xorOp(a, b):
            if a == 0 and b == 0:
                return 0
            elif a == 0 and b == 1:
                return 1
            elif a == 1 and b == 0:
                return 1
            else:
                return 0

        def bitwiseXor(num1, num2):
            bitPos = 0
            resultNum = 0
            while num1 > 0 or num2 > 0:
                bit1 = num1 % 2
                bit2 = num2 % 2
                bitResult = xorOp(bit1, bit2)
                resultNum += bitResult << bitPos
                num1 //= 2
                num2 //= 2
                bitPos += 1
            return resultNum

        indexI = totalCount - 1
        while True:
            if indexI < 0:
                break
            matrixA[indexI][indexI] = nums[indexI]
            matrixB[indexI][indexI] = nums[indexI]
            indexJ = indexI + 1
            while True:
                if indexJ == totalCount:
                    break
                leftXor = matrixA[indexI][indexJ - 1]
                rightXor = matrixA[indexI + 1][indexJ]
                xorValue = bitwiseXor(leftXor, rightXor)
                matrixA[indexI][indexJ] = xorValue

                firstVal = matrixA[indexI][indexJ]
                secondVal = matrixB[indexI][indexJ - 1]
                thirdVal = matrixB[indexI + 1][indexJ]

                maxLeft = maximum(firstVal, secondVal)
                overallMax = maximum(maxLeft, thirdVal)
                matrixB[indexI][indexJ] = overallMax

                indexJ += 1
            indexI -= 1

        # Helper to get number of pairs in queries
        def getPairCount(pairs):
            countPairs = 0
            while True:
                try:
                    pairs[countPairs]
                except IndexError:
                    break
                countPairs += 1
            return countPairs

        lengthQueries = getPairCount(queries)

        def getElement(a, b):
            return matrixB[a][b]

        resultList = []
        currentIdx = 0
        while currentIdx < lengthQueries:
            pairElement = queries[currentIdx]
            leftVal = pairElement[0]
            rightVal = pairElement[1]
            resultList.append(getElement(leftVal, rightVal))
            currentIdx += 1

        return resultList