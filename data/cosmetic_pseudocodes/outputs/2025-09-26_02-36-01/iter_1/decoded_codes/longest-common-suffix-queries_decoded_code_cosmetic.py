class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        suffixDictionary: dict[str, int] = {}

        for idx, currentWord in enumerate(wordsContainer):
            wordLen = len(currentWord)
            for startPos in range(wordLen):
                currentSuffix = currentWord[startPos:]
                if currentSuffix not in suffixDictionary:
                    suffixDictionary[currentSuffix] = idx
                else:
                    existingIndex = suffixDictionary[currentSuffix]
                    existingWord = wordsContainer[existingIndex]
                    existingWordLen = len(existingWord)
                    if wordLen < existingWordLen or (wordLen == existingWordLen and idx < existingIndex):
                        suffixDictionary[currentSuffix] = idx

        def get_best_match(query: str) -> int:
            qLen = len(query)
            for offset in range(qLen):
                suffixCandidate = query[offset:]
                if suffixCandidate in suffixDictionary:
                    return suffixDictionary[suffixCandidate]

            smallestIndex = 0
            for i in range(1, len(wordsContainer)):
                candidateWord = wordsContainer[i]
                smallestWord = wordsContainer[smallestIndex]
                if len(candidateWord) < len(smallestWord) or (len(candidateWord) == len(smallestWord) and i < smallestIndex):
                    smallestIndex = i
            return smallestIndex

        outputIndices: list[int] = []
        for queryElement in wordsQuery:
            outputIndices.append(get_best_match(queryElement))

        return outputIndices