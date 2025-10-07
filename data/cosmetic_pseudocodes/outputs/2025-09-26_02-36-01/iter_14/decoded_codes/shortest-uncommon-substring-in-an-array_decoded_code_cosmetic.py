from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def countAllSubstrings(collection: List[str]) -> dict:
            mapCounts = defaultdict(int)

            def addSubstrings(text: str) -> None:
                length = len(text)

                def addFromIndex(start: int, length: int) -> None:
                    if start >= length:
                        return

                    def scanSubstrings(endPos: int) -> None:
                        if endPos > length:
                            return
                        segment = text[start:endPos]
                        mapCounts[segment] += 1
                        scanSubstrings(endPos + 1)

                    scanSubstrings(start + 1)
                    addFromIndex(start + 1, length)

                addFromIndex(0, length)

            for item in collection:
                addSubstrings(item)
            return mapCounts

        def findShortestUnique(text: str, mapCounts: dict) -> str:
            n = len(text)
            result = ""

            def exploreStart(pos: int) -> None:
                nonlocal result
                if pos >= n:
                    return

                def exploreEnd(endPos: int) -> None:
                    nonlocal result
                    if endPos > n:
                        return
                    candidate = text[pos:endPos]
                    if mapCounts[candidate] == 1:
                        if (result == "") or (len(candidate) < len(result)) or (len(candidate) == len(result) and candidate < result):
                            result = candidate
                    exploreEnd(endPos + 1)

                exploreEnd(pos + 1)
                exploreStart(pos + 1)

            exploreStart(0)
            return result

        frequencyMap = countAllSubstrings(arr)
        answerList = []

        def processItems(items: List[str]) -> None:
            if not items:
                return
            current = items[0]
            shortest = findShortestUnique(current, frequencyMap)
            answerList.append(shortest)
            processItems(items[1:])

        processItems(arr)
        return answerList