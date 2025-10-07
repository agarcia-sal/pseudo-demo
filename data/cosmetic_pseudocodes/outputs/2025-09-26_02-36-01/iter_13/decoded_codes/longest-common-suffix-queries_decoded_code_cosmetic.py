from typing import List, Dict


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        indexBySuffix: Dict[str, int] = {}

        def compareIndices(existingIndex: int, candidateIndex: int) -> bool:
            existingWord = wordsContainer[existingIndex]
            candidateWord = wordsContainer[candidateIndex]
            if len(candidateWord) < len(existingWord):
                return True
            elif len(candidateWord) == len(existingWord):
                if candidateIndex < existingIndex:
                    return True
            return False

        def addSuffixes(word: str, wordIndex: int) -> None:
            def recurAdd(i: int) -> None:
                if i > len(word) - 1:
                    return
                currentSuffix = word[i:]
                if currentSuffix not in indexBySuffix:
                    indexBySuffix[currentSuffix] = wordIndex
                else:
                    if compareIndices(indexBySuffix[currentSuffix], wordIndex):
                        indexBySuffix[currentSuffix] = wordIndex
                recurAdd(i + 1)
            recurAdd(0)

        wordPos = 0
        while wordPos < len(wordsContainer):
            addSuffixes(wordsContainer[wordPos], wordPos)
            wordPos += 1

        def findBestMatch(query: str) -> int:
            pos = 0
            while True:
                if pos > len(query) - 1:
                    break
                currSuffix = query[pos:]
                if currSuffix in indexBySuffix:
                    return indexBySuffix[currSuffix]
                pos += 1

            def findMinIndex() -> int:
                minLength = len(wordsContainer[0])
                minIndex = 0

                def scan(i: int) -> None:
                    nonlocal minLength, minIndex
                    if i >= len(wordsContainer):
                        return
                    w = wordsContainer[i]
                    if len(w) < minLength:
                        minLength = len(w)
                        minIndex = i
                    elif len(w) == minLength:
                        if i < minIndex:
                            minIndex = i
                    scan(i + 1)
                scan(1)
                return minIndex

            return findMinIndex()

        answerList: List[int] = []

        def processQueries(index: int) -> None:
            if index >= len(wordsQuery):
                return
            res = findBestMatch(wordsQuery[index])
            answerList.append(res)
            processQueries(index + 1)

        processQueries(0)

        return answerList