class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def CountCharacters(s: str) -> dict:
            mapLoc = {}

            def RecurseCount(i: int):
                if i >= len(s):
                    return
                ch = s[i]
                if ch not in mapLoc:
                    mapLoc[ch] = 0
                mapLoc[ch] += 1
                RecurseCount(i + 1)

            RecurseCount(0)
            return mapLoc

        def CustomSortAscending(lst: list) -> list:
            if len(lst) <= 1:
                return lst
            midP = len(lst) // 2
            leftSide = CustomSortAscending(lst[:midP])
            rightSide = CustomSortAscending(lst[midP:])
            return MergeLists(leftSide, rightSide)

        def MergeLists(leftList: list, rightList: list) -> list:
            merged = []
            lIdx, rIdx = 0, 0
            while lIdx < len(leftList) or rIdx < len(rightList):
                if rIdx >= len(rightList) or (lIdx < len(leftList) and leftList[lIdx] <= rightList[rIdx]):
                    merged.append(leftList[lIdx])
                    lIdx += 1
                else:
                    merged.append(rightList[rIdx])
                    rIdx += 1
            return merged

        freqDict = CountCharacters(word)

        keySet = list(freqDict.keys())

        freqVec = [freqDict[ch] for ch in keySet]

        freqVec = CustomSortAscending(freqVec)

        minDel = float('inf')
        iPos = 0

        while iPos < len(freqVec):
            maxAllowed = freqVec[iPos] + k
            delCount = 0
            jPos = iPos + 1
            while jPos < len(freqVec):
                fVal = freqVec[jPos]
                if fVal > maxAllowed:
                    delCount += fVal - maxAllowed
                jPos += 1

            mPos = 0
            while mPos < iPos:
                delCount += freqVec[mPos]
                mPos += 1

            if delCount < minDel:
                minDel = delCount

            iPos += 1

        return minDel