import sys

class Solution:
    def minValidStrings(self, words, target):
        complexSet = set()
        for currentStr in words:
            for counterB in range(1, len(currentStr) + 1):
                complexSet.add(currentStr[0:counterB])

        limit = len(target)
        MAX_INT = sys.maxsize
        resultList = [MAX_INT] * (limit + 1)
        resultList[0] = 0  # (1 - 1) = 0

        for outerIndex in range(1, limit + 1):
            for innerIndex in range(outerIndex, 0, -1):
                subSegment = target[innerIndex - 1: outerIndex]
                if subSegment in complexSet:
                    previousValue = resultList[innerIndex - 1]
                    candidate = previousValue + 1
                    if candidate < resultList[outerIndex]:
                        resultList[outerIndex] = candidate

        return resultList[limit] if resultList[limit] != MAX_INT else -1