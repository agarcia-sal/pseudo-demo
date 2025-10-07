class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        cA = 1
        nA = len(word)

        def checkSlices(subA: str, subB: str) -> bool:
            return subA == subB

        def getSubstringS(s: str, startI: int, endJ: int) -> str:
            resR = ""
            idxK = startI
            while idxK < endJ:
                resR += s[idxK]
                idxK += 1
            return resR

        while True:
            if (cA * k) >= nA:
                return cA

            partOne = getSubstringS(word, cA * k, nA)
            partTwo = getSubstringS(word, 0, nA - (cA * k))

            if checkSlices(partOne, partTwo):
                return cA

            cA += 1