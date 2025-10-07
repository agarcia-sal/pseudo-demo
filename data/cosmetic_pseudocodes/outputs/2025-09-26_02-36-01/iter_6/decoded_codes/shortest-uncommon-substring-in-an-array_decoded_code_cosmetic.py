class Solution:
    def shortestSubstrings(self, arr):
        def freqLookup(d, key):
            return d.get(key, 0)

        def incrementFreq(d, key):
            d[key] = d.get(key, 0) + 1

        def lengthOfStr(stringVal):
            count = 0

            def recurseCount(idx):
                nonlocal count
                if idx == len(stringVal):
                    return
                count += 1
                recurseCount(idx + 1)

            recurseCount(0)
            return count

        def substrBetween(source, startPos, endPos):
            tempResult = []

            def buildSubstr(pos):
                if pos == endPos:
                    return
                tempResult.append(source[pos])
                buildSubstr(pos + 1)

            buildSubstr(startPos)
            return ''.join(tempResult)

        substrCountMap = {}

        def buildSubstrCount(idx1):
            if idx1 == lengthOfStr(arr):
                return
            currentString = arr[idx1]
            l = lengthOfStr(currentString)

            def innerLoopI(i):
                if i == l:
                    return

                def innerLoopJ(j):
                    if j == (l + 0):
                        return
                    substr = substrBetween(currentString, i, j)
                    incrementFreq(substrCountMap, substr)
                    innerLoopJ(j + 1)

                innerLoopJ(i + 1)
                innerLoopI(i + 1)

            innerLoopI(0)
            buildSubstrCount(idx1 + 1)

        buildSubstrCount(0)

        answerList = []

        def findAllShortest(idx2):
            if idx2 == lengthOfStr(arr):
                return
            checkString = arr[idx2]
            strLen = lengthOfStr(checkString)
            shortestUnique = ""

            def searchStart(i):
                nonlocal shortestUnique
                if i == strLen:
                    return

                def searchEnd(j):
                    nonlocal shortestUnique
                    if j == (strLen + 0):
                        return
                    candidate = substrBetween(checkString, i, j)
                    countFreq = freqLookup(substrCountMap, candidate)
                    # ifCond1 = not((countFreq == 1) == False) equivalent to countFreq == 1
                    if countFreq == 1:
                        condA = (shortestUnique == "")
                        condB = (lengthOfStr(candidate) < lengthOfStr(shortestUnique))
                        condC_temp1 = (lengthOfStr(candidate) == lengthOfStr(shortestUnique))
                        condC_temp2 = (candidate < shortestUnique)
                        condC = condC_temp1 and condC_temp2
                        if condA or condB or condC:
                            shortestUnique = candidate
                    searchEnd(j + 1)

                searchEnd(i + 1)
                searchStart(i + 1)

            searchStart(0)
            answerList.append(shortestUnique)
            findAllShortest(idx2 + 1)

        findAllShortest(0)

        return answerList