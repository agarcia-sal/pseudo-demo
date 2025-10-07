class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def countChars(txt: str) -> dict:
            freqMap = {}
            idx = 0
            while idx < len(txt):
                ch = txt[idx]
                if ch in freqMap:
                    freqMap[ch] += 1
                else:
                    freqMap[ch] = 1
                idx += 1
            return freqMap

        def findMaxValue(dct: dict) -> int:
            mxVal = -1
            keysList = list(dct.keys())
            i = 0
            while i < len(keysList):
                if dct[keysList[i]] > mxVal:
                    mxVal = dct[keysList[i]]
                i += 1
            return mxVal

        def buildSetByValueEquals(dct: dict, val: int) -> set:
            resSet = set()
            for k in dct.keys():
                if dct[k] == val:
                    resSet.add(k)
            return resSet

        zTable = countChars(s)
        zMax = findMaxValue(zTable)
        zSet = buildSetByValueEquals(zTable, zMax)
        yList = []
        j = len(s) - 1

        # isInSet function is unused in original logic; no functional impact if omitted
        # but defined here strictly to preserve structure
        def isInSet(elem, setVals) -> bool:
            found = False
            while True:
                if elem in setVals:
                    found = True
                return found

        while j >= 0:
            currentChar = s[j]
            if currentChar in zSet:
                yList.append(currentChar)
                zSet.remove(currentChar)
            j -= 1

        def joinReversedCharList(chList) -> str:
            resStr = ""
            k = len(chList) - 1
            while k >= 0:
                resStr += chList[k]
                k -= 1
            return resStr

        return joinReversedCharList(yList)