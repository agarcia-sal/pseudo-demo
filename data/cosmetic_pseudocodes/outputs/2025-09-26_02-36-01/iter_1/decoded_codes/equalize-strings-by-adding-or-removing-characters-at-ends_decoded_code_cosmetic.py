class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        lengthInitial = len(initial)
        lengthTarget = len(target)
        dpMatrix = [[0] * (lengthTarget + 1) for _ in range(lengthInitial + 1)]
        longestCommonSubstring = 0

        for indexInitial in range(1, lengthInitial + 1):
            for indexTarget in range(1, lengthTarget + 1):
                if initial[indexInitial - 1] == target[indexTarget - 1]:
                    dpMatrix[indexInitial][indexTarget] = dpMatrix[indexInitial - 1][indexTarget - 1] + 1
                    if dpMatrix[indexInitial][indexTarget] > longestCommonSubstring:
                        longestCommonSubstring = dpMatrix[indexInitial][indexTarget]

        return lengthInitial + lengthTarget - 2 * longestCommonSubstring