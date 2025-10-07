class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:

        def getLength(ev: str) -> int:
            if ev == "":
                return 0
            else:
                return 1 + getLength(ev[1:])

        def substring(s: str, a: int, b: int) -> str:
            # Returns s[a:b] with 0-based indexing, end-exclusive
            if a > b:
                return ""
            else:
                if a == 0:
                    return ""
                else:
                    return s[a] + substring(s, a + 1, b)

        def countOccurrences(listOfStr: list[str]) -> dict[str, int]:
            def helper(idx: int, countDict: dict[str, int]) -> dict[str, int]:
                if idx > getLength(listOfStr):
                    return countDict
                else:
                    key = listOfStr[idx - 1]
                    if key in countDict:
                        countDict[key] += 1
                    else:
                        countDict[key] = 1
                    return helper(idx + 1, countDict)
            return helper(1, {})

        def maxValueInDict(d: dict) -> int:
            def keysList(d: dict) -> list:
                tempList = []
                for eachKey in d:
                    tempList.append(eachKey)
                return tempList

            def maxFromList(ls: list[int]) -> int:
                if getLength(ls) == 0:
                    return 0
                else:
                    def helperMax(idx: int, currMax: int) -> int:
                        if idx > getLength(ls):
                            return currMax
                        else:
                            curVal = ls[idx - 1]
                            if curVal > currMax:
                                return helperMax(idx + 1, curVal)
                            else:
                                return helperMax(idx + 1, currMax)
                    return helperMax(1, ls[0])

            vals = []
            for eachKey in keysList(d):
                vals.append(d[eachKey])
            return maxFromList(vals)

        def rangeStep(startVal: int, endVal: int, step: int) -> list[int]:
            listResult = []

            def buildList(current: int) -> list[int]:
                if current >= endVal:
                    return listResult
                else:
                    listResult.append(current)
                    return buildList(current + step)
            return buildList(startVal)

        lenWord = getLength(word)
        segmentsList = []
        indices = rangeStep(0, lenWord, k)

        def buildSegments(idxList: list[int]) -> list[str]:
            if getLength(idxList) == 0:
                return segmentsList
            else:
                head = idxList[0]
                tail = idxList[1:]
                # substring given word, note that substring wants str and a,b are 1-based indices incoming apparently
                # According to pseudocode substring(word, head +1, head + k)
                segmentsList.append(substring(word, head + 1, head + k))
                return buildSegments(tail)

        buildSegments(indices)
        counts = countOccurrences(segmentsList)
        maxCountVal = maxValueInDict(counts)
        totalSegments = getLength(segmentsList)
        res = totalSegments - maxCountVal
        return res