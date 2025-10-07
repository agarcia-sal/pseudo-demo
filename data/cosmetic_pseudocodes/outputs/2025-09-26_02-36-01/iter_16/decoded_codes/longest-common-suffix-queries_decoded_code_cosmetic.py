from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        mapSuffixes: Dict[str, int] = {}

        def findMatch(word: str, idx: int) -> None:
            def recurse(i: int) -> None:
                if i > len(word) - 1:
                    return
                subSuffix = word[i:]
                if subSuffix not in mapSuffixes:
                    mapSuffixes[subSuffix] = idx
                else:
                    currentIdx = mapSuffixes[subSuffix]
                    currentWord = wordsContainer[currentIdx]
                    if (len(word) < len(currentWord)) or (len(word) == len(currentWord) and idx < currentIdx):
                        mapSuffixes[subSuffix] = idx
                recurse(i + 1)
            recurse(0)

        counter = 0
        while counter < len(wordsContainer):
            curWord = wordsContainer[counter]
            findMatch(curWord, counter)
            counter += 1

        def get_best_match(query: str) -> int:
            position = 0
            while position < len(query):
                querySuffix = query[position:]
                if querySuffix in mapSuffixes:
                    return mapSuffixes[querySuffix]
                position += 1

            minIndex = 0
            minWord = wordsContainer[0]
            minIter = 1
            while minIter < len(wordsContainer):
                cmpWord = wordsContainer[minIter]
                if (len(cmpWord) < len(minWord)) or (len(cmpWord) == len(minWord) and minIter < minIndex):
                    minIndex = minIter
                    minWord = cmpWord
                minIter += 1
            return minIndex

        outputResults = []
        idx = 0
        while idx < len(wordsQuery):
            queryItem = wordsQuery[idx]
            matchedIndex = get_best_match(queryItem)
            outputResults.append(matchedIndex)
            idx += 1
        return outputResults