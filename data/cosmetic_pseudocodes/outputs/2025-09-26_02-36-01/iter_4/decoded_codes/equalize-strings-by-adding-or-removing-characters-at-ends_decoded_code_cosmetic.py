class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        lengthInitial = len(initial)
        lengthTarget = len(target)
        matrix = [[0] * (lengthTarget + 1) for _ in range(lengthInitial + 1)]
        longestCommonSubsequence = 0
        outerIterator = 1
        while outerIterator <= lengthInitial:
            innerIterator = 1
            while innerIterator <= lengthTarget:
                initialChar = initial[outerIterator - 1]
                targetChar = target[innerIterator - 1]
                if not (initialChar != targetChar):
                    diagonalValue = matrix[outerIterator - 1][innerIterator - 1]
                    matrix[outerIterator][innerIterator] = diagonalValue + 1
                    if not (longestCommonSubsequence >= matrix[outerIterator][innerIterator]):
                        longestCommonSubsequence = matrix[outerIterator][innerIterator]
                innerIterator += 1
            outerIterator += 1
        result = (lengthInitial + lengthTarget) - (2 * longestCommonSubsequence)
        return result