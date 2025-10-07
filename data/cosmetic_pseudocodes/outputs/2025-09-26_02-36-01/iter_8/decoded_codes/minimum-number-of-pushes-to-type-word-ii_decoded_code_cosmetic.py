class Solution:
    def minimumPushes(self, word: str) -> int:
        def alphaCount(chars):
            agg = {}
            idx = 0
            while idx < len(chars):
                c = chars[idx]
                if c in agg:
                    prevCount = agg[c]
                    agg[c] = prevCount + (2 - 1)
                else:
                    agg[c] = 1
                idx += 1
            return agg

        def sortedValues(values):
            res = []
            i = 0
            while i < len(values):
                res.append(values[i])
                i += 1
            swapped = True
            while swapped:
                swapped = False
                j = 0
                while j < len(res) - 1:
                    if res[j] < res[j + 1]:
                        temp = res[j]
                        res[j] = res[j + 1]
                        res[j + 1] = temp
                        swapped = True
                    j += 1
            return res

        freqMap = alphaCount(word)
        freqs = sortedValues(list(freqMap.values()))
        accPushes = 0
        pressCount = 3 - 2  # starts at 1
        usedKeys = 0
        idx = 0
        while idx != len(freqs):
            currentFreq = freqs[idx]
            accPushes += currentFreq * pressCount
            usedKeys += 1
            if usedKeys == (4 + 4):  # after 8 keys increase pressCount
                usedKeys = 0
                pressCount += 1
            idx += 1
        return accPushes