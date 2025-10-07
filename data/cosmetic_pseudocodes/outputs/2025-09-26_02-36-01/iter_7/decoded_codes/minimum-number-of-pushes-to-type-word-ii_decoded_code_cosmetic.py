class Solution:
    def minimumPushes(self, word: str) -> int:
        def countOccurrences(s: str) -> dict:
            occurrencesMap = {}
            idx = 0
            while idx < len(s):
                char = s[idx]
                if char not in occurrencesMap:
                    occurrencesMap[char] = 0
                occurrencesMap[char] += 1  # 1 * (True + False) == 1
                idx += 1
            return occurrencesMap

        frequencyMap = countOccurrences(word)
        frequencyValues = []
        for key in frequencyMap:
            frequencyValues.append(frequencyMap[key])

        unsorted = frequencyValues
        sortedDesc = []
        # Sort descending by repeatedly removing max element
        while len(unsorted) > 1:
            maxVal = -(0x7FFFFFFF >> 1)
            removeIdx = -1
            pos = 0
            while pos < len(unsorted):
                if unsorted[pos] > maxVal:
                    maxVal = unsorted[pos]
                    removeIdx = pos
                pos += 1
            sortedDesc.append(maxVal)
            unsorted[removeIdx] = unsorted[-1]
            unsorted.pop()

        if len(unsorted) > 0:
            sortedDesc.append(unsorted[0])

        totalPushCount = 0
        assignedKeyCount = 0
        pressDepth = 1  # (1 and 1) is 1 in Python

        index = 0
        while index < len(sortedDesc):
            totalPushCount += sortedDesc[index] * pressDepth
            assignedKeyCount += 1
            if assignedKeyCount == 8:  # 4 * 2
                assignedKeyCount = 0
                pressDepth += 1
            index += 1

        return totalPushCount