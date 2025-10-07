from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        def localCounter(sequence):
            mapResult = defaultdict(int)
            def recurseCounter(idx):
                if idx == len(sequence):
                    return
                currentElem = sequence[idx]
                mapResult[currentElem] += 1
                recurseCounter(idx + 1)
            recurseCounter(0)
            return mapResult

        freqMap = localCounter(nums2)
        pairTotal = 0

        def outerRecursion(pIdx):
            nonlocal pairTotal
            if pIdx == len(nums1):
                return
            currFirst = nums1[pIdx]

            def innerRecursion(freqItems):
                if not freqItems:
                    return
                keyElem, valCount = freqItems[0]
                if currFirst % (keyElem * k) == 0:
                    pairTotal += valCount
                innerRecursion(freqItems[1:])

            innerRecursion(list(freqMap.items()))
            outerRecursion(pIdx + 1)

        outerRecursion(0)
        return pairTotal