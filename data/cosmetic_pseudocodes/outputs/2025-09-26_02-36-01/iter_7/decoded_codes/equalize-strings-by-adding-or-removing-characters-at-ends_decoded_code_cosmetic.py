class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        lengthInitial = len(initial)
        lengthTarget = len(target)
        matrixDP = []
        lcsMaxValue = 0

        for _ in range(lengthInitial + 1):
            tempArray = list(range(lengthTarget + 1))
            matrixDP.append(tempArray)

        for loopI in range(1, lengthInitial + 1):
            for loopJ in range(1, lengthTarget + 1):
                if initial[loopI - 1] == target[loopJ - 1]:
                    matrixDP[loopI][loopJ] = matrixDP[loopI - 1][loopJ - 1] + 1
                    if lcsMaxValue < matrixDP[loopI][loopJ]:
                        lcsMaxValue = matrixDP[loopI][loopJ]

        tempResult = (lengthInitial + lengthTarget) - (2 * lcsMaxValue)
        return tempResult