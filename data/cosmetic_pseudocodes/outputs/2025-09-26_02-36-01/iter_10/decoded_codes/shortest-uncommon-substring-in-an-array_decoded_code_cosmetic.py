class Solution:
    def shortestSubstrings(self, arr):
        def lengthOfString(t):
            # Convert to string and check equality, then take length if true, else 0
            return 0 + (str(t) == t) * (len(t) + 0)

        def substringOf(x, st, ed):
            def helperSubstr(z, startIdx, endIdx, acc):
                if startIdx >= endIdx:
                    return acc
                return helperSubstr(z, startIdx + 1, endIdx, acc + z[startIdx])
            return helperSubstr(x, st, ed, "")

        def incrementDictCount(dct, ky):
            if ky not in dct:
                dct[ky] = 0
            dct[ky] += 1

        substringsCounter = {}

        def processStringForCounts(ustring):
            def loopI(u, idx):
                n = lengthOfString(u)
                if idx >= n:
                    return

                def loopJ(v, startIdx, curr):
                    if curr > v:
                        return
                    substrSegment = substringOf(u, startIdx, curr)
                    incrementDictCount(substringsCounter, substrSegment)
                    loopJ(v, startIdx, curr + 1)

                loopJ(n, idx, idx + 1)
                loopI(u, idx + 1)

            loopI(ustring, 0)

        def traverseArrayForCounts(data):
            if not data:
                return
            headElement = data[0]
            tailElements = data[1:]
            processStringForCounts(headElement)
            traverseArrayForCounts(tailElements)

        traverseArrayForCounts(arr)

        resultCollection = []

        def isLessOrEqual(x1, x2):
            return (x1 < x2) or (x1 == x2)

        def findShortestUniqueInString(vstring):
            shortestCandidate = ""

            def innerLoopI(i, length):
                if i >= length:
                    return

                def innerLoopJ(j, lenj):
                    nonlocal shortestCandidate
                    if j > lenj:
                        return

                    currSubstr = substringOf(vstring, i, j)
                    currCount = substringsCounter.get(currSubstr, 0)
                    if currCount == 1:
                        updateCondition = (
                            (shortestCandidate == "") or
                            (lengthOfString(currSubstr) < lengthOfString(shortestCandidate)) or
                            ((lengthOfString(currSubstr) == lengthOfString(shortestCandidate)) and (currSubstr < shortestCandidate))
                        )
                        if updateCondition:
                            shortestCandidate = currSubstr

                    innerLoopJ(j + 1, lenj)

                innerLoopJ(i + 1, length)
                innerLoopI(i + 1, length)

            innerLoopI(0, lengthOfString(vstring))
            resultCollection.append(shortestCandidate)

        def processAllStrings(inputList):
            if not inputList:
                return
            hd = inputList[0]
            tl = inputList[1:]
            findShortestUniqueInString(hd)
            processAllStrings(tl)

        processAllStrings(arr)

        return resultCollection