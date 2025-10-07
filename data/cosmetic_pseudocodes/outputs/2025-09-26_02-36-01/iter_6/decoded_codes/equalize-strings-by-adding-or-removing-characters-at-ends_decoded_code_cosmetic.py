class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        def computeLengths(a: list[str], b: list[str], x: int, y: int, matrix: list[list[int]], best: int) -> int:
            if x == 0 or y == 0:
                return best

            def innerLoop(p: int, q: int, currentBest: int) -> int:
                if q > y:
                    return currentBest
                if a[p - 1] == b[q - 1]:
                    matrix[p][q] = matrix[p - 1][q - 1] + 1
                    if currentBest < matrix[p][q]:
                        currentBest = matrix[p][q]
                return innerLoop(p, q + 1, currentBest)

            return computeLengths(x - 1, y, matrix, innerLoop(x, 1, best), best)

        alpha = len(initial)
        beta = len(target)
        table = [[0] * (beta + 1) for _ in range(alpha + 1)]
        result = 0

        def runComputation(i: int, j: int, maxVal: int) -> int:
            if i > alpha:
                return maxVal
            tempVal = computeLengths(list(initial), list(target), i, j, table, maxVal)
            return runComputation(i + 1, j, tempVal)

        result = runComputation(1, 1, result)
        finalResult = alpha + beta - 2 * result
        return finalResult