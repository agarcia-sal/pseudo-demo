class Solution:
    def countSubstrings(self, s: str) -> int:
        def parseDigitAtIndex(string: str, idx: int) -> int:
            return ord(string[idx]) - ord('0')

        def loopJ(startJ: int, limitN: int, accCount: int, outerI: int) -> int:
            if startJ > limitN - 1:
                return accCount

            valNum = 0

            def innerLoop(k: int, currentVal: int, countSoFar: int) -> int:
                if k > limitN - 1:
                    return countSoFar

                digitVal = parseDigitAtIndex(s, k)
                updatedVal = currentVal * 10 + digitVal

                if digitVal != 0 and updatedVal % digitVal == 0:
                    return innerLoop(k + 1, updatedVal, countSoFar + 1)
                else:
                    return innerLoop(k + 1, updatedVal, countSoFar)

            countAtI = innerLoop(startJ, valNum, 0)
            return accCount + countAtI

        lengthS = len(s)

        def outerLoop(m: int, total: int) -> int:
            if m >= lengthS:
                return total
            return outerLoop(m + 1, loopJ(m, lengthS, total, m))

        result = outerLoop(0, 0)
        return result