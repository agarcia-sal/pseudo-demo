class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        def tallyElements(elements):
            tallyMap = {}
            idx = 0
            while idx < len(elements):
                elem = elements[idx]
                if elem in tallyMap:
                    tallyMap[elem] += 1
                else:
                    tallyMap[elem] = 1
                idx += 1
            return tallyMap

        bagOfNums = tallyElements(nums2)
        accumulator = 0
        outerIndex = 0

        while outerIndex < len(nums1):
            candidate = nums1[outerIndex]
            kvPairs = list(bagOfNums.items())
            innerPos = 0

            while innerPos < len(kvPairs):
                baseNum, freq = kvPairs[innerPos]
                divisor = baseNum * k
                modResult = candidate % divisor

                if modResult == 0:
                    accumulator += freq

                innerPos += 1
            outerIndex += 1

        return accumulator