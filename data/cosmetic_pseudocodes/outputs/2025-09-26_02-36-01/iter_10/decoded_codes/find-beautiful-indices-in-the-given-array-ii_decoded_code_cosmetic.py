class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def subEquals(strX: str, startX: int, patternX: str) -> bool:
            def loopRec(lim: int, cur: int) -> bool:
                if cur > lim:
                    return True
                if strX[cur] != patternX[cur - startX]:
                    return False
                return loopRec(lim, cur + 1)

            if len(patternX) == 0:
                return True
            if startX < 0:
                return False
            if startX + len(patternX) - 1 >= len(strX):
                return False
            return loopRec(startX + len(patternX) - 1, startX)

        def assembleIndices(stringP: str, patternP: str) -> list[int]:
            accumulatorList = []
            pos = 0
            limit = len(stringP) - len(patternP)
            while pos <= limit:
                if subEquals(stringP, pos, patternP):
                    accumulatorList.append(pos)
                pos += 1
            return accumulatorList

        listAlpha = assembleIndices(s, a)
        listBeta = assembleIndices(s, b)
        resultRound = []

        leftIdx = 0
        rightIdx = 0

        def absVal(x: int) -> int:
            return x if x >= 0 else -x

        while leftIdx < len(listAlpha) and rightIdx < len(listBeta):
            diff = absVal(listAlpha[leftIdx] - listBeta[rightIdx])
            if diff <= k:
                resultRound.append(listAlpha[leftIdx])
                leftIdx += 1
            else:
                if listAlpha[leftIdx] < listBeta[rightIdx]:
                    leftIdx += 1
                else:
                    rightIdx += 1

        return resultRound