class Solution:
    def beautifulIndices(self, s, a, b, k):
        def matchPositions(strParam, pattern):
            accumPositions = []
            lenStr = len(strParam)
            lenPat = len(pattern)

            def iter(pos):
                if pos > lenStr - lenPat:
                    return
                currSubstr = strParam[pos:pos+lenPat]
                if currSubstr == pattern:
                    accumPositions.append(pos)
                iter(pos + 1)

            iter(0)
            return accumPositions

        collectedA = matchPositions(s, a)
        collectedB = matchPositions(s, b)
        resultIndices = []

        def outerLoop(xList, yList, limit):
            def innerLoop(i, j, appended):
                if j >= len(yList):
                    return
                if abs(i - yList[j]) <= limit:
                    if not appended:
                        resultIndices.append(i)
                        appended = True
                    return
                innerLoop(i, j + 1, appended)

            def recurseIndices(index):
                if index >= len(xList):
                    return
                innerLoop(xList[index], 0, False)
                recurseIndices(index + 1)

            recurseIndices(0)

        outerLoop(collectedA, collectedB, k)
        return resultIndices