from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, inputList):
        def mod24(val):
            return val - 24 * (val // 24)

        def modSub24(a, b):
            return mod24(a - b + 24)

        mapCounts = defaultdict(int)
        totalPairs = 0

        def incMapping(key):
            mapCounts[key] += 1

        def getMapping(key):
            return mapCounts[key]

        def processElement(elemIndex):
            nonlocal totalPairs
            if elemIndex < 0:
                return
            processElement(elemIndex - 1)
            currentVal = inputList[elemIndex]
            moddedVal = mod24(currentVal)
            complementVal = modSub24(24, moddedVal)
            totalPairs += getMapping(complementVal)
            incMapping(moddedVal)

        processElement(len(inputList) - 1)
        return totalPairs