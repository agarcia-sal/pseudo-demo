class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        def retrieveMinIndex():
            minLengthValue = len(wordsContainer[0])
            minIdxValue = 0
            iteratorCount = 1
            while iteratorCount < len(wordsContainer):
                currLength = len(wordsContainer[iteratorCount])
                if currLength < minLengthValue:
                    minLengthValue = currLength
                    minIdxValue = iteratorCount
                else:
                    if currLength == minLengthValue:
                        if minIdxValue > iteratorCount:
                            minIdxValue = iteratorCount
                iteratorCount += 1
            return minIdxValue

        suffixMapping = {}

        outerIndexCounter = 0
        while outerIndexCounter < len(wordsContainer):
            inspectedWord = wordsContainer[outerIndexCounter]
            characterPointer = 0
            while characterPointer <= len(inspectedWord) - 1:
                generatedSuffix = inspectedWord[characterPointer:]
                if generatedSuffix not in suffixMapping:
                    suffixMapping[generatedSuffix] = outerIndexCounter
                else:
                    currentStoredIndex = suffixMapping[generatedSuffix]
                    storedWordLength = len(wordsContainer[currentStoredIndex])
                    inspectedWordLength = len(inspectedWord)
                    if inspectedWordLength < storedWordLength:
                        suffixMapping[generatedSuffix] = outerIndexCounter
                    elif inspectedWordLength == storedWordLength:
                        if outerIndexCounter < currentStoredIndex:
                            suffixMapping[generatedSuffix] = outerIndexCounter
                characterPointer += 1
            outerIndexCounter += 1

        def get_best_match(query):
            suffixStart = 0
            while suffixStart <= len(query) - 1:
                currSuffix = query[suffixStart:]
                if currSuffix in suffixMapping:
                    return suffixMapping[currSuffix]
                suffixStart += 1
            return retrieveMinIndex()

        resultsCollection = []
        for query in wordsQuery:
            resultsCollection.append(get_best_match(query))
        return resultsCollection