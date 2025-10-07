class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        lengthA = len(initial)
        lengthB = len(target)
        matrix = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]
        longestCommonSubsequence = 0
        rowIndex = 1
        while rowIndex <= lengthA:
            colIndex = 1
            while colIndex <= lengthB:
                charInitial = initial[rowIndex - 1]
                charTarget = target[colIndex - 1]
                if charInitial == charTarget:
                    prevValue = matrix[rowIndex - 1][colIndex - 1]
                    currentValue = prevValue + 1
                    matrix[rowIndex][colIndex] = currentValue
                    if longestCommonSubsequence < currentValue:
                        longestCommonSubsequence = currentValue
                colIndex += 1
            rowIndex += 1
        sumLengths = lengthA + lengthB
        result = sumLengths - (2 * longestCommonSubsequence)
        return result