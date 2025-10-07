class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        suffixIndices = {}

        containerLength = len(wordsContainer)
        currentWordIndex = 0

        while currentWordIndex < containerLength:
            currentWord = wordsContainer[currentWordIndex]
            positionInWord = 0
            wordLength = len(currentWord)

            while positionInWord < wordLength:
                currentSuffix = currentWord[positionInWord:]
                if currentSuffix not in suffixIndices:
                    suffixIndices[currentSuffix] = currentWordIndex
                else:
                    recordedIndex = suffixIndices[currentSuffix]
                    recordedWord = wordsContainer[recordedIndex]
                    recordedLength = len(recordedWord)
                    if (wordLength < recordedLength) or ((wordLength == recordedLength) and (currentWordIndex < recordedIndex)):
                        suffixIndices[currentSuffix] = currentWordIndex
                positionInWord += 1
            currentWordIndex += 1

        def get_best_match(query: str) -> int:
            posInQuery = 0
            lengthOfQuery = len(query)
            while posInQuery < lengthOfQuery:
                suffixSubstring = query[posInQuery:]
                if suffixSubstring in suffixIndices:
                    return suffixIndices[suffixSubstring]
                posInQuery += 1

            minimumIdx = 0
            minLength = len(wordsContainer[0])
            indexCheck = 1
            totalWordsCount = len(wordsContainer)
            while indexCheck < totalWordsCount:
                checkWordLength = len(wordsContainer[indexCheck])
                if (checkWordLength < minLength) or ((checkWordLength == minLength) and (indexCheck < minimumIdx)):
                    minimumIdx = indexCheck
                    minLength = checkWordLength
                indexCheck += 1

            return minimumIdx

        outputList = []
        queriesCount = len(wordsQuery)
        qIndex = 0

        while qIndex < queriesCount:
            currentQuery = wordsQuery[qIndex]
            matchIndex = get_best_match(currentQuery)
            outputList.append(matchIndex)
            qIndex += 1

        return outputList