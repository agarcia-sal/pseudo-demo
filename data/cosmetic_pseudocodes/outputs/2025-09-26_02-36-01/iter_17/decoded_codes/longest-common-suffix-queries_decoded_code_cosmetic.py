from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        suffixMap: Dict[str, int] = {}
        outerCounter = 0

        while outerCounter < len(wordsContainer):
            currentWord = wordsContainer[outerCounter]
            innerCounter = 0
            while innerCounter < len(currentWord):
                currentSuffix = currentWord[innerCounter:]
                if currentSuffix not in suffixMap:
                    suffixMap[currentSuffix] = outerCounter
                else:
                    mappedIndex = suffixMap[currentSuffix]
                    mappedWord = wordsContainer[mappedIndex]
                    cond1 = len(currentWord) < len(mappedWord)
                    cond2 = (len(currentWord) == len(mappedWord)) and (outerCounter < mappedIndex)
                    if cond1 or cond2:
                        suffixMap[currentSuffix] = outerCounter
                innerCounter += 1
            outerCounter += 1

        def get_best_match(query: str) -> int:
            position = 0
            foundIndex = -1
            while foundIndex == -1 and position < len(query):
                sub = query[position:]
                if sub in suffixMap:
                    foundIndex = suffixMap[sub]
                else:
                    position += 1

            if foundIndex != -1:
                return foundIndex
            else:
                bestIndex = 0
                bestLength = len(wordsContainer[0])
                idx = 1
                while idx < len(wordsContainer):
                    currentLength = len(wordsContainer[idx])
                    if (currentLength < bestLength) or (currentLength == bestLength and idx < bestIndex):
                        bestIndex = idx
                        bestLength = currentLength
                    idx += 1
                return bestIndex

        outputList: List[int] = []
        queryIter = 0
        while queryIter < len(wordsQuery):
            currentQuery = wordsQuery[queryIter]
            matchIndex = get_best_match(currentQuery)
            outputList.append(matchIndex)
            queryIter += 1

        return outputList