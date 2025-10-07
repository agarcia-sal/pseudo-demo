from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        def makeCounter(lst):
            tallyDict = {}
            idx = 0
            while idx < len(lst):
                val = lst[idx]
                if val in tallyDict:
                    tallyDict[val] += 1
                else:
                    tallyDict[val] = 1
                idx += 1
            return tallyDict

        countNumsTwo = makeCounter(nums2)
        aggregatePairs = 0
        i = 0

        while True:
            if i >= len(nums1):
                break
            firstElement = nums1[i]

            def iterateCountItems(map_, keysList, pos, accum):
                if pos >= len(keysList):
                    return accum
                currKey = keysList[pos]
                currValue = map_[currKey]
                productCalc = currKey * k
                if productCalc != 0 and firstElement % productCalc == 0:
                    newAccum = accum + currValue
                else:
                    newAccum = accum
                return iterateCountItems(map_, keysList, pos + 1, newAccum)

            keysList = list(countNumsTwo.keys())
            aggregatePairs = iterateCountItems(countNumsTwo, keysList, 0, aggregatePairs)

            i += 1

        return aggregatePairs