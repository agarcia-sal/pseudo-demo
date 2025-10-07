from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        deltaDict: Dict[str, int] = {}

        for z, currentWord in enumerate(wordsContainer):
            for y in range(len(currentWord)):
                partialSuffix = currentWord[y:]
                if partialSuffix not in deltaDict:
                    deltaDict[partialSuffix] = z
                else:
                    oldIndex = deltaDict[partialSuffix]
                    oldWord = wordsContainer[oldIndex]
                    if (len(currentWord) < len(oldWord)) or (len(currentWord) == len(oldWord) and z < oldIndex):
                        deltaDict[partialSuffix] = z

        def get_best_match(query: str) -> int:
            for c in range(len(query)):
                candidateSuffix = query[c:]
                if candidateSuffix in deltaDict:
                    return deltaDict[candidateSuffix]

            shortestIndex = 0
            for x in range(1, len(wordsContainer)):
                if (len(wordsContainer[x]) < len(wordsContainer[shortestIndex])) or \
                   (len(wordsContainer[x]) == len(wordsContainer[shortestIndex]) and x < shortestIndex):
                    shortestIndex = x
            return shortestIndex

        accumulator: List[int] = []
        for candidateQuery in wordsQuery:
            accumulator.append(get_best_match(candidateQuery))

        return accumulator