class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        suffixIndexMap = {}

        def processWordSuffixes(currentWord: str, currentIndex: int, position: int) -> None:
            if position >= len(currentWord):
                return
            currentSuffix = currentWord[position:]
            if currentSuffix not in suffixIndexMap:
                suffixIndexMap[currentSuffix] = currentIndex
            else:
                mappedIndex = suffixIndexMap[currentSuffix]
                mappedWord = wordsContainer[mappedIndex]
                lenCurrWord = len(currentWord)
                lenMappedWord = len(mappedWord)
                if (lenCurrWord < lenMappedWord) or (lenCurrWord == lenMappedWord and currentIndex < mappedIndex):
                    suffixIndexMap[currentSuffix] = currentIndex
            processWordSuffixes(currentWord, currentIndex, position + 1)

        def processAllWords(position: int) -> None:
            if position >= len(wordsContainer):
                return
            runningWord = wordsContainer[position]
            processWordSuffixes(runningWord, position, 0)
            processAllWords(position + 1)

        processAllWords(0)

        def get_best_match(query: str) -> int:
            def searchSuffix(pos: int) -> int:
                if pos >= len(query):
                    candidateLengths = [len(word) for word in wordsContainer]
                    minLength = candidateLengths[0]
                    minIndex = 0
                    idx = 1
                    while idx < len(candidateLengths):
                        if candidateLengths[idx] < minLength:
                            minLength = candidateLengths[idx]
                            minIndex = idx
                        elif candidateLengths[idx] == minLength and idx < minIndex:
                            minIndex = idx
                        idx += 1
                    return minIndex

                suffixCheck = query[pos:]
                if suffixCheck in suffixIndexMap:
                    return suffixIndexMap[suffixCheck]
                else:
                    return searchSuffix(pos + 1)

            return searchSuffix(0)

        resultCollection = []
        queryCursor = 0
        while queryCursor < len(wordsQuery):
            currentQuery = wordsQuery[queryCursor]
            bestIdx = get_best_match(currentQuery)
            resultCollection.append(bestIdx)
            queryCursor += 1
        return resultCollection