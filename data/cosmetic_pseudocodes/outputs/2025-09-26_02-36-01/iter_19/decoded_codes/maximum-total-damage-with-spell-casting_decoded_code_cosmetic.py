class Solution:
    def maximumTotalDamage(self, power):
        def maxVal(a, b):
            return a if a > b else b

        def getAt(m, k):
            return m[k] if k in m else 0

        countMap = {}
        idx = 0
        while idx < len(power):
            curr = power[idx]
            countMap[curr] = countMap.get(curr, 0) + 1
            idx += 1

        keysList = list(countMap.keys())
        keysList.sort()

        dpMap = {}
        n = len(keysList)

        def loop(i):
            if i == n:
                return
            currKey = keysList[i]

            excVal = getAt(dpMap, keysList[i - 1]) if i > 0 else 0
            incVal = currKey * getAt(countMap, currKey)

            j2 = i - 1
            while j2 >= 0 and keysList[j2] >= currKey - 2:
                j2 -= 1

            if j2 >= 0:
                incVal += getAt(dpMap, keysList[j2])

            dpMap[currKey] = maxVal(incVal, excVal)

            loop(i + 1)

        loop(0)

        maxDmg = 0
        for v in dpMap:
            if dpMap[v] > maxDmg:
                maxDmg = dpMap[v]

        return maxDmg