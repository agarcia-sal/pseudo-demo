class Solution:
    def maximumTotalDamage(self, power):
        def computeCount(arr):
            def helper(i, m):
                if i >= len(arr):
                    return m
                else:
                    key = arr[i]
                    val = 1
                    if key in m:
                        val = m[key] + 1
                    newMap = copyMap(m)
                    newMap[key] = val
                    return helper(i + 1, newMap)
            return helper(0, self.emptyMap())

        def copyMap(original):
            newM = self.emptyMap()
            keysList = keysOf(original)
            l = len(keysList)
            r = 0
            while True:
                if r >= l:
                    break
                k = keysList[r]
                newM[k] = original[k]
                r += 1
            return newM

        def keysOf(m):
            ks = self.emptyList()
            for k in iterateKeys(m):
                ks.append(k)
            return ks

        def insertionSort(arr):
            def insert(sorted_list, val):
                if len(sorted_list) == 0:
                    return [val]
                elif val < sorted_list[0]:
                    return prepend(val, sorted_list)
                else:
                    rest = insert(sorted_list[1:], val)
                    return prepend(sorted_list[0], rest)

            def helperSort(i, res):
                if i >= len(arr):
                    return res
                else:
                    return helperSort(i + 1, insert(res, arr[i]))

            return helperSort(0, self.emptyList())

        def prepend(x, lst):
            newL = self.emptyList()
            newL.append(x)
            idx = 0
            while idx < len(lst):
                newL.append(lst[idx])
                idx += 1
            return newL

        def iterateKeys(m):
            i = 0
            keysList = []
            for k in m:
                if i >= len(keysList):
                    keysList.append(k)
                else:
                    keysList[i] = k
                i += 1
            return keysList

        countMap = computeCount(power)
        uniqueList = keysOf(countMap)
        sortedUnique = insertionSort(uniqueList)

        dpMap = self.emptyMap()
        n = len(sortedUnique)
        idx = 0
        while True:
            if idx >= n:
                break
            pwr = sortedUnique[idx]

            excludeVal = 0
            if idx > 0:
                keyL = sortedUnique[idx - 1]
                if keyL in dpMap:
                    excludeVal = dpMap[keyL]

            countVal = 0
            if pwr in countMap:
                countVal = countMap[pwr]

            includeVal = pwr * countVal

            j = idx - 1
            while j >= 0 and sortedUnique[j] >= (pwr - 2):
                j -= 1

            if j >= 0:
                beforeKey = sortedUnique[j]
                if beforeKey in dpMap:
                    includeVal += dpMap[beforeKey]

            if includeVal > excludeVal:
                dpMap[pwr] = includeVal
            else:
                dpMap[pwr] = excludeVal

            idx += 1

        valuesList = self.emptyList()
        for k in iterateKeys(dpMap):
            valuesList.append(dpMap[k])

        return self.maxInList(valuesList)

    def maxInList(self, lst):
        if len(lst) == 0:
            return 0

        def helper(i, currentMax):
            if i >= len(lst):
                return currentMax
            else:
                newMax = currentMax
                if lst[i] > currentMax:
                    newMax = lst[i]
                return helper(i + 1, newMax)

        return helper(0, lst[0])

    def emptyMap(self):
        return self.newMap()

    def newMap(self):
        return {}

    def emptyList(self):
        return []

    def append(self, lst, val):
        lst[len(lst):] = [val]

    def slice(self, lst, start, endIndex):
        res = self.emptyList()
        i = start
        while i < endIndex:
            res.append(lst[i])
            i += 1
        return res

    def iterateKeys(self, m):
        i = 0
        keysList = []
        for k in m:
            if i >= len(keysList):
                keysList.append(k)
            else:
                keysList[i] = k
            i += 1
        return keysList