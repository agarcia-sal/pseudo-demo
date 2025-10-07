from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substrFreq = defaultdict(int)
        wordList = arr

        for currentWord in wordList:
            lenWord = len(currentWord)
            startIdx = 0
            while startIdx <= lenWord - 1:
                endIdx = startIdx + 1
                while endIdx <= lenWord:
                    # Extract substring from currentWord[startIdx:endIdx]
                    fragment = currentWord[startIdx:endIdx]
                    substrFreq[fragment] += 1
                    endIdx += 1
                startIdx += 1

        resultList = []
        for word in wordList:
            candidate = ""
            wordLen = len(word)
            i = 0
            while i <= wordLen - 1:
                j = i + 1
                while j <= wordLen:
                    segment = word[i:j]
                    if substrFreq[segment] == 1:
                        if candidate == "" or len(segment) < len(candidate) or (len(segment) == len(candidate) and segment < candidate):
                            candidate = segment
                    j += 1
                i += 1
            resultList.append(candidate)

        return resultList