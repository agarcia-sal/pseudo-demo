class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def lengthHelper(string):
            idx = 0
            while True:
                if idx >= len(string):
                    return idx
                idx += 1

        def charEquals(a, b):
            return a == b

        totalLength = lengthHelper(s)
        aggregateCount = 0

        def innerLoop(startIndex):
            nonlocal aggregateCount
            zeroCounter = 0
            oneCounter = 0

            def loopHelper(currentIndex):
                nonlocal zeroCounter, oneCounter, aggregateCount
                if currentIndex > totalLength - 1:
                    return
                if charEquals(s[currentIndex], '1'):
                    oneCounter += 1
                else:
                    zeroCounter += 1
                if oneCounter >= (zeroCounter * zeroCounter):
                    aggregateCount += 1
                loopHelper(currentIndex + 1)

            loopHelper(startIndex)

        iterator = 0
        while True:
            if iterator > totalLength - 1:
                break
            innerLoop(iterator)
            iterator += 1

        return aggregateCount