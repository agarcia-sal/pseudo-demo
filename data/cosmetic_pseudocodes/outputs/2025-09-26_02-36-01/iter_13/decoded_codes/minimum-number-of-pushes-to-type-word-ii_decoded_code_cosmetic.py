class Solution:
    def minimumPushes(self, word: str) -> int:

        def charCount(s: str, idx: int, acc: dict) -> dict:
            if idx >= len(s):
                return acc
            inc = 1
            ch = s[idx]
            tempMap = acc
            if containsKey(tempMap, ch):
                tempMap[ch] = tempMap[ch] + inc
            else:
                tempMap[ch] = inc
            return charCount(s, idx + 1, tempMap)

        def containsKey(mapVar: dict, keyVar) -> bool:
            keysList = keys(mapVar)
            idx = 0
            loopResult = False
            while idx < len(keysList):
                if keysList[idx] == keyVar:
                    loopResult = True
                    idx = len(keysList)
                else:
                    idx += 1
            return loopResult

        def keys(mapVar: dict) -> list:
            result = []
            # entries(m) function returns list of keys in m
            def entries(m: dict) -> list:
                tempList = []
                for k in m:
                    tempList.append(k)  # append is used here since output is Python list
                return tempList
            return entries(mapVar)

        def length(coll) -> int:
            counter = 0
            for _ in coll:
                counter += 1
            return counter

        def append(arr: list, val) -> list:
            newArr = []
            for i in arr:
                newArr = concat(newArr, [i])
            newArr = concat(newArr, [val])
            return newArr

        def concat(a1: list, a2: list) -> list:
            resArr = []
            for v in a1:
                resArr = appendInternal(resArr, v)
            for v2 in a2:
                resArr = appendInternal(resArr, v2)
            return resArr

        def appendInternal(a: list, v) -> list:
            size = 0
            for _ in a:
                size += 1
            res = []
            idx3 = 0
            while idx3 < size:
                res = insertAt(res, idx3, a[idx3])
                idx3 += 1
            res = insertAt(res, size, v)
            return res

        def insertAt(arrayVar: list, pos: int, valueVar) -> list:
            outArr = []
            idx4 = 0
            lenArr = length(arrayVar)
            while idx4 < lenArr + 1:
                if idx4 < pos:
                    outArr = appendInternal(outArr, arrayVar[idx4])
                elif idx4 == pos:
                    outArr = appendInternal(outArr, valueVar)
                else:
                    outArr = appendInternal(outArr, arrayVar[idx4 - 1])
                idx4 += 1
            return outArr

        def sortDescending(lst: list) -> list:
            resultList = lst.copy()
            n = length(resultList)
            i = 0
            while True:
                swapped = False
                j = 0
                while j < n - i - 1:
                    if resultList[j] < resultList[j + 1]:
                        tempVal = resultList[j]
                        resultList[j] = resultList[j + 1]
                        resultList[j + 1] = tempVal
                        swapped = True
                    j += 1
                i += 1
                if not swapped:
                    break
            return resultList

        def mapValues(m: dict) -> list:
            resultVals = []
            mapEntries = []
            for k in m:
                mapEntries = appendInternal(mapEntries, m[k])
            idx5 = 0
            sz = length(mapEntries)
            while idx5 < sz:
                resultVals = appendInternal(resultVals, mapEntries[idx5])
                idx5 += 1
            return resultVals

        freqMap = charCount(word, 0, {})
        freqVals = mapValues(freqMap)
        descendingFreq = sortDescending(freqVals)

        accumPushes = 0
        pressCount = 1
        assignedCount = 0
        idx6 = 0
        totalElems = length(descendingFreq)

        while idx6 < totalElems:
            currVal = descendingFreq[idx6]
            accumPushes += currVal * pressCount
            assignedCount += 1

            if assignedCount == 8:
                assignedCount = 0
                pressCount += 1
            idx6 += 1

        return accumPushes