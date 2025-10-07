class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        def iterateEnd(startIndex: int, accCount: int) -> int:
            def step(i: int, onesAcc: int, zerosAcc: int, countAcc: int) -> int:
                if i > n - 1:
                    return countAcc
                if s[i] == '1':
                    updatedOnes = onesAcc + 1
                    updatedZeros = zerosAcc
                else:
                    updatedOnes = onesAcc
                    updatedZeros = zerosAcc + 1
                if updatedOnes >= updatedZeros * updatedZeros:
                    newCount = countAcc + 1
                else:
                    newCount = countAcc
                return step(i + 1, updatedOnes, updatedZeros, newCount)

            return step(startIndex, 0, 0, accCount)

        def iterateStart(j: int, total: int) -> int:
            if j > n - 1:
                return total
            newTotal = iterateEnd(j, total)
            return iterateStart(j + 1, newTotal)

        return iterateStart(0, 0)