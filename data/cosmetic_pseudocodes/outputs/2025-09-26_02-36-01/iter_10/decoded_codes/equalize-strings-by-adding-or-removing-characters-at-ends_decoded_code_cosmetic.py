class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        alpha = len(initial)
        beta = len(target)
        table = [[0] * (beta + 1) for _ in range(alpha + 1)]
        peak_lcs = 0

        def processIndices(x: int, y: int) -> None:
            nonlocal peak_lcs
            if x > alpha:
                return
            if y > beta:
                processIndices(x + 1, 1)
                return
            if initial[x - 1] == target[y - 1]:
                table[x][y] = table[x - 1][y - 1] + 1
                if peak_lcs < table[x][y]:
                    peak_lcs = table[x][y]
            processIndices(x, y + 1)

        processIndices(1, 1)
        return alpha + beta - 2 * peak_lcs