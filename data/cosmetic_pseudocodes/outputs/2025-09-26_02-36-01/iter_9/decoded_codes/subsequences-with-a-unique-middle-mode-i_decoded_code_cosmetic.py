class Solution:
    def subsequencesWithMiddleMode(self, lamda):
        bignum = 10**10 + 7
        tx = 0
        cgap = 1
        allsub = []

        def genCombs(arr, k, idx, path):
            if k == 0:
                allsub.append(path)
                return
            if idx >= len(arr):
                return
            genCombs(arr, k - 1, idx + 1, path + [arr[idx]])
            genCombs(arr, k, idx + 1, path)

        xlen = 0
        while xlen < len(lamda):
            xlen += 1

        if xlen < 5:
            return 0

        genCombs(lamda, 5, 0, [])

        def countFrequencies(lst):
            freqMap = {}
            i = 0
            while i < len(lst):
                el = lst[i]
                curCount = freqMap.get(el, 0)
                freqMap[el] = curCount + 1
                i += 1
            return freqMap

        acc = 0
        subsIdx = 0
        while subsIdx < len(allsub):
            currentSub = allsub[subsIdx]
            freqTable = countFrequencies(currentSub)
            midVal = currentSub[2]
            midFreq = freqTable[midVal]

            modeUnique = True
            keys = list(freqTable.keys())
            kIdx = 0
            while kIdx < len(keys) and modeUnique:
                numero = keys[kIdx]
                counter = freqTable[numero]
                if numero != midVal and counter >= midFreq:
                    modeUnique = False
                kIdx += 1

            if modeUnique:
                acc += 1

            subsIdx += 1

        res = acc - (acc // bignum) * bignum
        return res