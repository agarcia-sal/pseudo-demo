class Solution:
    def beautifulIndices(self, x, y, z, w):
        def eqSubstr(source, startIdx, target, count):
            for idx in range(count):
                if source[startIdx + idx] != target[idx]:
                    return False
            return True

        def extractPositions(string, pattern, resultList):
            strLen, patLen = len(string), len(pattern)
            cursor = 0
            while cursor <= strLen - patLen:
                if eqSubstr(string, cursor, pattern, patLen):
                    resultList.append(cursor)
                cursor += 1

        def absDiff(a, b):
            return a - b if a >= b else b - a

        positionsY = []
        positionsZ = []
        extractPositions(x, y, positionsY)
        extractPositions(x, z, positionsZ)

        def hasClosePosition(ele, candidates, limit):
            for p in candidates:
                if absDiff(ele, p) <= limit:
                    return True
            return False

        answerList = []
        for pos in positionsY:
            if hasClosePosition(pos, positionsZ, w):
                answerList.append(pos)

        return answerList