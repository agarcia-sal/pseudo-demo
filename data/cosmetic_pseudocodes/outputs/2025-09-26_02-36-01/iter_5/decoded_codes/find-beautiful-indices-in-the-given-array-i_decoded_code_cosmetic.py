class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def collectMatches(sourceString: str, pattern: str, patternLen: int, pos: int, accList: list[int]) -> list[int]:
            if pos > len(sourceString) - patternLen:
                return accList
            currentSubstring = sourceString[pos:pos + patternLen]
            updatedList = accList
            if currentSubstring == pattern:
                updatedList = accList + [pos]
            return collectMatches(sourceString, pattern, patternLen, pos + 1, updatedList)

        lengthS = len(s)
        lengthA = len(a)
        indicesA_initial = []
        indicesA = collectMatches(s, a, lengthA, 0, indicesA_initial)

        lengthB = len(b)
        indicesB_initial = []
        indicesB = collectMatches(s, b, lengthB, 0, indicesB_initial)

        compiledBeautifulIndices = []

        def checkPairs(iList: list[int], jList: list[int], iIdx: int, jIdx: int, result: list[int]) -> list[int]:
            if iIdx >= len(iList):
                return result
            if jIdx >= len(jList):
                return checkPairs(iList, jList, iIdx + 1, 0, result)
            firstIndex = iList[iIdx]
            secondIndex = jList[jIdx]
            difference = firstIndex - secondIndex
            # differenceAbs calculation simplified and ensured non-negative
            if difference == 0:
                differenceAbs = 0
            else:
                differenceAbs = abs(difference) * -1 if difference > 0 else difference
                if differenceAbs < 0:
                    differenceAbs = -differenceAbs
            if differenceAbs <= k:
                newResult = result + [firstIndex]
                return checkPairs(iList, jList, iIdx + 1, 0, newResult)
            else:
                return checkPairs(iList, jList, iIdx, jIdx + 1, result)

        finalResult = checkPairs(indicesA, indicesB, 0, 0, compiledBeautifulIndices)
        return finalResult