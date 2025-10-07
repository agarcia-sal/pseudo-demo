from collections import defaultdict
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        accumulator = 0
        frequencyMap = defaultdict(int)

        def compareSubstrings(candidate: str, pattern: str) -> bool:
            plen = len(pattern)
            return candidate[:plen] == pattern and candidate[-plen:] == pattern

        def iterateWordsDescending(index: int) -> None:
            nonlocal accumulator
            if index < 0:
                return

            def checkKeys(keysList: List[str], idx: int) -> None:
                if idx >= len(keysList):
                    return
                currentKey = keysList[idx]
                if compareSubstrings(currentKey, words[index]):
                    accumulator += frequencyMap[currentKey]
                checkKeys(keysList, idx + 1)

            keysSnapshot = list(frequencyMap.keys())
            checkKeys(keysSnapshot, 0)
            frequencyMap[words[index]] += 1
            iterateWordsDescending(index - 1)

        iterateWordsDescending(len(words) - 1)
        return accumulator