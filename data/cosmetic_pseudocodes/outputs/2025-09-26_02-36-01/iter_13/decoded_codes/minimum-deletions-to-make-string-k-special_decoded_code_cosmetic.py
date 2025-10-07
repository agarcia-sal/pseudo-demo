class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def countCharacters(s: str) -> dict:
            def incCount(d: dict, key: str):
                if key not in d:
                    d[key] = 1
                else:
                    d[key] += 1

            freqDict = {}
            pos = 0
            while True:
                if pos >= len(s):
                    break
                incCount(freqDict, s[pos])
                pos += 1
            return freqDict

        def toList(d: dict) -> list:
            lst = []
            keys = list(d.keys())
            i = 0
            while i < len(keys):
                lst.append(d[keys[i]])
                i += 1
            return lst

        def sortAscending(arr: list) -> list:
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            less = []
            greaterOrEqual = []
            idx = 1
            while idx < len(arr):
                if arr[idx] < pivot:
                    less.append(arr[idx])
                else:
                    greaterOrEqual.append(arr[idx])
                idx += 1
            return sortAscending(less) + [pivot] + sortAscending(greaterOrEqual)

        # helpers assumed from pseudocode replaced by python idioms:
        # existsKey -> key in dict
        # getKey -> dict[key]
        # setKey -> dict[key] = val
        # getKeys -> dict.keys()
        # emptyMap -> {}
        # emptyList -> []

        freqMap = countCharacters(word)
        freqValues = toList(freqMap)
        freqValues = sortAscending(freqValues)
        inf = float('inf')
        minDel = inf

        def recurLoop(idx: int, arr: list, n: int, kVal: int, currentMin: int) -> int:
            if idx >= n:
                return currentMin

            maxAllowed = arr[idx] + kVal
            delAcc = 0

            def calcDeletionsFrom(arrInner: list, startPos: int, endPos: int, maxA: int) -> int:
                totalDel = 0
                pos2 = startPos
                while pos2 <= endPos:
                    if arrInner[pos2] > maxA:
                        totalDel += arrInner[pos2] - maxA
                    pos2 += 1
                return totalDel

            iterPos = idx + 1
            delAcc += calcDeletionsFrom(arr, iterPos, n - 1, maxAllowed)

            def sumListSegment(arrSegment: list, beginI: int, endI: int) -> int:
                sumVal = 0
                jj = beginI
                while jj <= endI:
                    sumVal += arrSegment[jj]
                    jj += 1
                return sumVal

            if idx > 0:
                delAcc += sumListSegment(arr, 0, idx - 1)

            if delAcc < currentMin:
                currentMin = delAcc

            return recurLoop(idx + 1, arr, n, kVal, currentMin)

        lengthVals = len(freqValues)
        return recurLoop(0, freqValues, lengthVals, k, minDel)