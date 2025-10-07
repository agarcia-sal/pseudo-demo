from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        mapCounts = defaultdict(int)

        def addSubstrings(s: str, startPos: int) -> None:
            if startPos == len(s):
                return
            endPos = startPos + 1
            while endPos <= len(s):
                currentPiece = s[startPos:endPos]
                mapCounts[currentPiece] += 1
                endPos += 1
            addSubstrings(s, startPos + 1)

        for element in arr:
            addSubstrings(element, 0)

        finalList = []

        def findUniqueMin(s: str, pos: int, currentBest: str) -> str:
            if pos == len(s):
                return currentBest
            pointer = pos + 1
            while pointer <= len(s):
                candidate = s[pos:pointer]
                if mapCounts[candidate] == 1:
                    if (currentBest == "" or 
                        len(candidate) < len(currentBest) or 
                        (len(candidate) == len(currentBest) and candidate < currentBest)):
                        currentBest = candidate
                pointer += 1
            return findUniqueMin(s, pos + 1, currentBest)

        for strItem in arr:
            candidateMin = ""
            candidateMin = findUniqueMin(strItem, 0, candidateMin)
            finalList.append(candidateMin)

        return finalList