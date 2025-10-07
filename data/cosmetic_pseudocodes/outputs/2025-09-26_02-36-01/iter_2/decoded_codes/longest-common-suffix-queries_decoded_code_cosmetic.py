from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        suffixDictionary = {}

        for pos, currentWord in enumerate(wordsContainer):
            for charIndex in range(len(currentWord)):
                subStr = currentWord[charIndex:]
                if subStr not in suffixDictionary:
                    suffixDictionary[subStr] = pos
                else:
                    mappedIdx = suffixDictionary[subStr]
                    storedWord = wordsContainer[mappedIdx]
                    if (len(currentWord) < len(storedWord)) or \
                       (len(currentWord) == len(storedWord) and pos < mappedIdx):
                        suffixDictionary[subStr] = pos

        def get_best_match(query: str) -> int:
            for startPos in range(len(query)):
                trialSuffix = query[startPos:]
                if trialSuffix in suffixDictionary:
                    return suffixDictionary[trialSuffix]

            minLen = float('inf')
            minIndex = -1
            for idx, candidate in enumerate(wordsContainer):
                candidateLength = len(candidate)
                if candidateLength < minLen or (candidateLength == minLen and idx < minIndex):
                    minLen = candidateLength
                    minIndex = idx
            return minIndex

        answers = []
        for q in wordsQuery:
            matchedIdx = get_best_match(q)
            answers.append(matchedIdx)
        return answers