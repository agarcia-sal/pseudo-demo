class Solution:
    def maximumLength(self, nums):
        freqMap = {}
        for val in nums:
            freqMap[val] = freqMap.get(val, 0) + 1

        storedLengths = {}

        def recurse(z):
            if (z not in freqMap) or (freqMap[z] < 2):
                if (z in freqMap) and (freqMap[z] >= 1):
                    return 1
                else:
                    return 0
            if z in storedLengths:
                return storedLengths[z]
            squared = z * z
            storedLengths[z] = recurse(squared) + 2
            return storedLengths[z]

        result = 1
        keyCollection = list(freqMap.keys())
        index = 0

        while index < len(keyCollection):
            element = keyCollection[index]
            if element == 1:
                times = freqMap[element]
                adjustment = times - 1 - ((times % 2) * 2)
                if adjustment > result:
                    result = adjustment
            else:
                candidate = recurse(element)
                if candidate > result:
                    result = candidate
            index += 1

        return result