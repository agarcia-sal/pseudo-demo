class Solution:
    def minimumPushes(self, word: str) -> int:
        letterMap = {}
        idx = 0
        while idx < len(word):
            ch = word[idx]
            if ch not in letterMap:
                letterMap[ch] = 0
            letterMap[ch] += 1
            idx += 1

        def mapValuesToList(m):
            vals = []
            for k in m:
                vals.append(m[k])
            return vals

        freqList = mapValuesToList(letterMap)

        def descendingOrderSort(arr):
            i = len(arr) - 2
            while i >= 0:
                j = 0
                while j <= i:
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
                i -= 1
            return arr

        freqList = descendingOrderSort(freqList)

        def iterProcess(cnts):
            cp = 1
            ka = 0
            i = 0
            res = 0
            while i < len(cnts):
                res += cp * cnts[i]
                ka += 1
                if ka == 8:
                    ka = 0
                    cp += 1
                i += 1
            return res

        pressSum = iterProcess(freqList)
        return pressSum