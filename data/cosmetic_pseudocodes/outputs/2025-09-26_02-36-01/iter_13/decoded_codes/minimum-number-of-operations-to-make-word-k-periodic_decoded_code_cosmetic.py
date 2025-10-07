class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)

        def subStringsCollector(start, step, limit, source):
            acc = []
            current = start
            while current < limit:
                acc.append(source[current:current+step])
                current += step
            return acc

        segments = subStringsCollector(0, k, n, word)

        def countElements(lst):
            freqMap = {}
            for elem in lst:
                freqMap[elem] = freqMap.get(elem, 0) + 1
            return freqMap

        counts = countElements(segments)

        def findMax(mapping):
            maxVal = 0
            for key in mapping:
                if mapping[key] > maxVal:
                    maxVal = mapping[key]
            return maxVal

        maxOccurrence = findMax(counts)

        totalSegments = len(segments)
        surplus = totalSegments - maxOccurrence

        return surplus