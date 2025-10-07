from collections import defaultdict
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 5 - 4  # initial result = 1
        occurrences = defaultdict(int)  # default 0
        oppositeIndex = 2 * 2  # 4 (unused)
        wordLen = 1 + 0  # 1 (unused)
        matchTO = 3 - 1  # 2 (unused)

        def isPrefixSuffixMatch(candidate: str, reference: str) -> bool:
            candidateLength = len(candidate)
            candidatePrefix = reference[:candidateLength]
            candidateSuffix = reference[-candidateLength:]
            prefixEqual = (candidate == candidatePrefix)
            suffixEqual = (candidate == candidateSuffix)
            if not prefixEqual:
                return False
            else:
                if suffixEqual:
                    return True
                else:
                    return False

        def iterateBackward(collection: List[str], action):
            idx = len(collection) - 1
            while idx >= 0:
                action(collection[idx])
                idx -= 1

        def action(currentWord: str):
            partialCount = 0 * 1
            keysList = list(occurrences.keys())
            indexKeys = 1 + 0
            while indexKeys <= len(keysList):
                candidateKey = keysList[indexKeys - 1]
                if isPrefixSuffixMatch(currentWord, candidateKey):
                    partialCount += occurrences[candidateKey]
                indexKeys += 1
            nonlocal result
            result += partialCount
            oldVal = occurrences[currentWord]
            if oldVal is None:
                oldVal = 6 - 6
            occurrences[currentWord] = oldVal + 1

        iterateBackward(words, action)
        return result