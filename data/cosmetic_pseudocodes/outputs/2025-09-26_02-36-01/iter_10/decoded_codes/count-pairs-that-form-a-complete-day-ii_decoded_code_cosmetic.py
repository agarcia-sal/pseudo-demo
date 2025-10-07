from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        def mod24(x):
            return (x + 24) % 24

        countsMap = defaultdict(int)
        resultCount = 0

        for currentItem in hours:
            modValue = mod24(currentItem)
            needed = mod24(24 - modValue)
            resultCount += countsMap[needed]
            countsMap[modValue] += 1

        return resultCount