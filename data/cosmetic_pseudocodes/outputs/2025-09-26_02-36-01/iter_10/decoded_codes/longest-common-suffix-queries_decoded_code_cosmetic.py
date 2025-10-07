from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        def isSmaller(x: int, y: int) -> bool:
            return x < y

        def minimalIndex(container: List[str]) -> int:
            smallestIdx = 0
            smallestLength = len(container[0])
            pos = 1
            while pos < len(container):
                if len(container[pos]) < smallestLength or (len(container[pos]) == smallestLength and isSmaller(pos, smallestIdx)):
                    smallestLength = len(container[pos])
                    smallestIdx = pos
                pos += 1
            return smallestIdx

        def subStr(s: str, startPos: int) -> str:
            # Return suffix of s starting at startPos
            return s[startPos:]

        m = dict()

        def updateMap(wrd: str, idx: int) -> None:
            j = 0
            n = len(wrd)
            while j < n:
                fragment = subStr(wrd, j)
                if fragment not in m:
                    m[fragment] = idx
                else:
                    oldIdx = m[fragment]
                    oldWord = wordsContainer[oldIdx]
                    if len(wrd) < len(oldWord) or (len(wrd) == len(oldWord) and idx < oldIdx):
                        m[fragment] = idx
                j += 1

        p = 0
        while p < len(wordsContainer):
            updateMap(wordsContainer[p], p)
            p += 1

        def get_best_match(query: str) -> int:
            i = 0
            n = len(query)
            while i < n:
                suffix = subStr(query, i)
                if suffix in m:
                    return m[suffix]
                i += 1
            return minimalIndex(wordsContainer)

        accumulator = []
        for q in wordsQuery:
            val = get_best_match(q)
            accumulator.append(val)
        return accumulator