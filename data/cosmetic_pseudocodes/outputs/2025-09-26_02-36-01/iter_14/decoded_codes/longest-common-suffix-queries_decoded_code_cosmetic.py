from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        mapSuffixes: Dict[str, int] = {}

        def assign_suffixes(posIdx: int, currentWord: str, originIdx: int) -> None:
            if posIdx > len(currentWord) - 1:
                return
            subStr = currentWord[posIdx:]
            if subStr not in mapSuffixes:
                mapSuffixes[subStr] = originIdx
            else:
                recordedIdx = mapSuffixes[subStr]
                wordAtRecorded = wordsContainer[recordedIdx]
                # Prefer the word with smaller length, or if equal length, smaller index
                if (len(currentWord) < len(wordAtRecorded)) or \
                   (len(currentWord) == len(wordAtRecorded) and originIdx < recordedIdx):
                    mapSuffixes[subStr] = originIdx
            assign_suffixes(posIdx + 1, currentWord, originIdx)

        def process_word(idxOuter: int) -> None:
            if idxOuter >= len(wordsContainer):
                return
            assign_suffixes(0, wordsContainer[idxOuter], idxOuter)
            process_word(idxOuter + 1)

        process_word(0)

        def minimal_index() -> int:
            minIdx = 0
            minLength = len(wordsContainer[0])
            currIdx = 1
            while currIdx < len(wordsContainer):
                currWordLength = len(wordsContainer[currIdx])
                if (currWordLength < minLength) or \
                   (currWordLength == minLength and currIdx < minIdx):
                    minIdx = currIdx
                    minLength = currWordLength
                currIdx += 1
            return minIdx

        def get_best_match(queryStr: str) -> int:
            pos = 0
            while pos < len(queryStr):
                subSuf = queryStr[pos:]
                if subSuf in mapSuffixes:
                    return mapSuffixes[subSuf]
                pos += 1
            return minimal_index()

        answer: List[int] = []
        idxQ = 0
        while idxQ < len(wordsQuery):
            currentQuery = wordsQuery[idxQ]
            answer.append(get_best_match(currentQuery))
            idxQ += 1

        return answer