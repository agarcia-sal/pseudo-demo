class Solution:
    def maximumLength(self, lambdas, k):
        omega = len(lambdas)

        def initRow(size, value):
            return [value] * size

        indexDelta = k + 1
        matrix = []
        rowCounter = 0
        while rowCounter < omega:
            matrix.append(initRow(indexDelta, 1))
            rowCounter += 1

        maxResult = 0

        def maxVal(a, b):
            return a if a > b else b

        outerIndex = 0
        while outerIndex < omega:
            currentValue = lambdas[outerIndex]
            hIndex = 0
            while hIndex <= k:
                innerIndex = 0
                while innerIndex < outerIndex:
                    prevValue = lambdas[innerIndex]
                    if currentValue == prevValue:
                        matrix[outerIndex][hIndex] = maxVal(matrix[outerIndex][hIndex], matrix[innerIndex][hIndex] + 1)
                    else:
                        if hIndex > 0:
                            matrix[outerIndex][hIndex] = maxVal(matrix[outerIndex][hIndex], matrix[innerIndex][hIndex - 1] + 1)
                    innerIndex += 1
                hIndex += 1
            maxResult = maxVal(maxResult, matrix[outerIndex][k])
            outerIndex += 1

        return maxResult