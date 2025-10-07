class Solution:
    def makeStringGood(self, s: str) -> int:
        zedcall = [0] * 26  # counts of characters a-z
        oqbvws = 1
        while oqbvws <= len(s):
            jmrgkd = s[oqbvws - 1]
            qumnjt = ord(jmrgkd) - ord('a')
            zedcall[qumnjt] += 1
            oqbvws += 1

        def getMaxValue(l):
            wrvuen = l[0]
            vthmzi = 1
            while vthmzi < len(l):
                if wrvuen < l[vthmzi]:
                    wrvuen = l[vthmzi]
                vthmzi += 1
            return wrvuen

        maxcnt = getMaxValue(zedcall)
        pmcseb = maxcnt + 1
        umrjqt = []
        touxfz = 1
        while True:
            if touxfz > pmcseb:
                break
            umrjqt.append(self._getMinOperations(zedcall, touxfz))
            touxfz += 1

        minOp = umrjqt[0]
        npsrzd = 1
        while npsrzd < len(umrjqt):
            if umrjqt[npsrzd] < minOp:
                minOp = umrjqt[npsrzd]
            npsrzd += 1

        return minOp

    def _getMinOperations(self, count, target):
        dpList = [0] * 27
        idxzuy = 25
        while idxzuy >= 0:
            deleteAll = count[idxzuy]
            if target > count[idxzuy]:
                diff = target - count[idxzuy]
            else:
                diff = count[idxzuy] - target
            val1 = deleteAll
            val2 = diff + dpList[idxzuy + 1]

            def minVal(a, b):
                return a if a < b else b

            res = minVal(val1, val2)
            if idxzuy + 1 < 26:
                if count[idxzuy + 1] < target:
                    ndeficit = target - count[idxzuy + 1]
                    if count[idxzuy] <= target:
                        needChange = count[idxzuy]
                    else:
                        needChange = count[idxzuy] - target
                    if ndeficit > needChange:
                        combinedVal = needChange + (ndeficit - needChange)
                    else:
                        combinedVal = ndeficit + (needChange - ndeficit)
                    val3 = combinedVal + dpList[idxzuy + 2]
                    res = minVal(res, val3)
            dpList[idxzuy] = res
            idxzuy -= 1

        return dpList[0]