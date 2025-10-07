class Solution:
    def answerString(self, alpha: str, beta: int) -> str:
        if beta == 1:
            return alpha
        else:
            def computeLastSubstring(omega: str) -> str:
                n = len(omega)

                def lastSub(idxB: int, idxC: int, countZ: int) -> int:
                    while True:
                        if idxC + countZ >= n:
                            return idxB
                        if omega[idxB + countZ] == omega[idxC + countZ]:
                            countZ += 1
                        elif omega[idxB + countZ] > omega[idxC + countZ]:
                            idxC = idxC + countZ + 1
                            countZ = 0
                        else:
                            newB = max(idxB + countZ + 1, idxC)
                            idxC = newB + 1
                            idxB = newB
                            countZ = 0

                pos = lastSub(0, 1, 0)
                return omega[pos:]

            subStr = computeLastSubstring(alpha)
            limit = len(alpha) - beta + 1
            endPos = len(subStr) if len(subStr) < limit else limit
            return subStr[:endPos]