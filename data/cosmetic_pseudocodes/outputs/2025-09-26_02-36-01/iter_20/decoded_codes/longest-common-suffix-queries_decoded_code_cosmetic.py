class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:

        def identicalDictCreator() -> dict[str, int]:
            return {}

        def substringExtractor(str_: str, startIdx: int) -> str:
            return str_[startIdx:]

        def stringLengthEqualOrSmaller(lenA: int, lenB: int, idxA: int, idxB: int) -> bool:
            if lenA < lenB:
                return True
            elif lenA == lenB:
                return idxA < idxB
            else:
                return False

        def selectMinimumIndex(words: list[str]) -> int:
            accIdx = 0
            accLen = len(words[0])
            current = 1
            while current < len(words):
                currLen = len(words[current])
                if currLen < accLen:
                    accLen = currLen
                    accIdx = current
                elif currLen == accLen and current < accIdx:
                    accIdx = current
                current += 1
            return accIdx

        def getBestMatchFunction(q: str, mapZ: dict[str, int]) -> int:
            lenQ = len(q)
            ptrA = 0
            while ptrA < lenQ:
                suff = substringExtractor(q, ptrA)
                if suff in mapZ:
                    return mapZ[suff]
                ptrA += 1
            return selectMinimumIndex(wordsContainer)

        mapAlpha = identicalDictCreator()

        idxOuter = 0
        while idxOuter < len(wordsContainer):
            wordCurr = wordsContainer[idxOuter]
            lenCurr = len(wordCurr)
            idxInner = 0
            while idxInner <= lenCurr - 1:
                substrCurr = substringExtractor(wordCurr, idxInner)
                if substrCurr not in mapAlpha:
                    mapAlpha[substrCurr] = idxOuter
                else:
                    existIdx = mapAlpha[substrCurr]
                    existWord = wordsContainer[existIdx]
                    if stringLengthEqualOrSmaller(lenCurr, len(existWord), idxOuter, existIdx):
                        mapAlpha[substrCurr] = idxOuter
                idxInner += 1
            idxOuter += 1

        outList = []
        idxQ = 0
        while idxQ < len(wordsQuery):
            queryWord = wordsQuery[idxQ]
            answerIdx = getBestMatchFunction(queryWord, mapAlpha)
            outList.append(answerIdx)
            idxQ += 1

        return outList