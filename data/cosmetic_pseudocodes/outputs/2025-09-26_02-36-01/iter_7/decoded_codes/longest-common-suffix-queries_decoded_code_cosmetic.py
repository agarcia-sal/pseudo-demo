class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        suffixIndexMap = {}

        def traverseSuffixes(currentWord: str, currentIndex: int) -> None:
            position = len(currentWord) - 1
            while position >= 0:
                currentSuffix = currentWord[position:]
                if currentSuffix not in suffixIndexMap:
                    suffixIndexMap[currentSuffix] = currentIndex
                else:
                    previousIndex = suffixIndexMap[currentSuffix]
                    previousWord = wordsContainer[previousIndex]
                    if (len(currentWord) < len(previousWord)) or (
                        len(currentWord) == len(previousWord) and currentIndex < previousIndex
                    ):
                        suffixIndexMap[currentSuffix] = currentIndex
                position -= 1

        totalWords = len(wordsContainer)
        for iterIndex in range(totalWords):
            traverseSuffixes(wordsContainer[iterIndex], iterIndex)

        def get_best_match(query: str) -> int:
            queryLength = len(query)
            startPos = 0
            while startPos < queryLength:
                currentSuffix = query[startPos:]
                if currentSuffix in suffixIndexMap:
                    return suffixIndexMap[currentSuffix]
                startPos += 1

            minimalIndex = 0
            minimalLength = len(wordsContainer[0])
            for searchPos in range(1, totalWords):
                candidateLength = len(wordsContainer[searchPos])
                if (candidateLength < minimalLength) or (
                    candidateLength == minimalLength and searchPos < minimalIndex
                ):
                    minimalIndex = searchPos
                    minimalLength = candidateLength
            return minimalIndex

        resultList = []
        queriesCount = len(wordsQuery)
        queryIter = 0
        while True:
            if queryIter >= queriesCount:
                break
            currentQuery = wordsQuery[queryIter]
            resultList.append(get_best_match(currentQuery))
            queryIter += 1

        return resultList