class Solution:
    def minOperations(self, pivotString: str, anchorString: str) -> int:
        def createZeroMatrix(rows: int, cols: int) -> list:
            return [[0] * cols for _ in range(rows)]

        def characterMatch(a: str, indexA: int, b: str, indexB: int) -> bool:
            return a[indexA] == b[indexB]

        lengthPivot = len(pivotString)
        lengthAnchor = len(anchorString)

        matrixDP = createZeroMatrix(lengthPivot + 1, lengthAnchor + 1)
        highestCommon = 0

        indexOuter = 1
        while indexOuter <= lengthPivot:
            indexInnerTemp = 1
            while indexInnerTemp <= lengthAnchor:
                if characterMatch(pivotString, indexOuter - 1, anchorString, indexInnerTemp - 1):
                    newValue = matrixDP[indexOuter - 1][indexInnerTemp - 1] + 1
                    if highestCommon < newValue:
                        highestCommon = newValue
                    matrixDP[indexOuter][indexInnerTemp] = newValue
                indexInnerTemp += 1
            indexOuter += 1

        sumLengths = lengthPivot + lengthAnchor
        adjustment = 2 * highestCommon

        return sumLengths - adjustment