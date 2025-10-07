class Solution:
    def minValidStrings(self, words, target):
        # words: list of strings
        # target: string

        def containsSubstring(coll, val):
            foundFlag = False

            def recurCheck(idx, limit):
                nonlocal foundFlag
                if idx > limit:
                    return
                if coll[idx - 1] == val:
                    foundFlag = True
                    return
                recurCheck(idx + 1, limit)

            recurCheck(1, len(coll))
            return foundFlag

        accumPrefixes = set()

        def gatherPrefixes(idxList, currentIdx):
            if currentIdx > len(idxList):
                return
            currWord = idxList[currentIdx - 1]

            def insertPrefix(pos):
                if pos > len(currWord):
                    return
                currPrefix = currWord[:pos]
                accumPrefixes.add(currPrefix)
                insertPrefix(pos + 1)

            insertPrefix(1)
            gatherPrefixes(idxList, currentIdx + 1)

        gatherPrefixes(words, 1)

        targetLen = len(target)
        INF = (1 * (2 ** 31) - (2 ** 31)) + (1 * (2 ** 31))  # positive infinity representation
        dpTable = [INF] * (targetLen + 1)
        dpTable[0] = 0

        def measurePosition(endPos):
            if endPos > targetLen:
                return

            def checkStart(startPos):
                if startPos > endPos:
                    return
                currFragment = target[startPos - 1:endPos]
                existsInPrefix = currFragment in accumPrefixes
                if existsInPrefix:
                    priorVal = dpTable[startPos - 1] + 1
                    if priorVal < dpTable[endPos]:
                        dpTable[endPos] = priorVal
                checkStart(startPos + 1)

            checkStart(1)
            measurePosition(endPos + 1)

        measurePosition(1)

        if dpTable[targetLen] != INF:
            return dpTable[targetLen]
        return -1