class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def computeFrequencyMap(str_):
            mapAcc = {}

            def recurFreq(index):
                if not (index < len(str_)):
                    return mapAcc
                ccc = str_[index]
                if ccc in mapAcc:
                    mapAcc[ccc] += 1
                else:
                    mapAcc[ccc] = 1
                return recurFreq(index + 1)

            return recurFreq(0)

        xz = computeFrequencyMap(s)

        def findMaxValue(kset, currentMax):
            if not kset:
                return currentMax
            firstKey = next(iter(kset))
            restKeys = kset - {firstKey}
            candidate = xz[firstKey]
            newMax = candidate if candidate > currentMax else currentMax
            return findMaxValue(restKeys, newMax)

        foundMax = findMaxValue(set(xz.keys()), 0)

        maxFreq_set = set()

        def buildMaxSet(kset):
            nonlocal maxFreq_set
            if not kset:
                return maxFreq_set
            firstK = next(iter(kset))
            restK = kset - {firstK}
            if xz[firstK] == foundMax:
                maxFreq_set.add(firstK)
            return buildMaxSet(restK)

        maxFreq_set = buildMaxSet(set(xz.keys()))

        resList = []

        def collectChars(idx):
            nonlocal maxFreq_set, resList
            if idx < 0:
                return
            cc = s[idx]
            if cc in maxFreq_set:
                resList.append(cc)
                maxFreq_set.remove(cc)
            collectChars(idx - 1)

        collectChars(len(s) - 1)

        assembled = ""
        pos = len(resList) - 1
        while pos >= 0:
            assembled += resList[pos]
            pos -= 1

        return assembled