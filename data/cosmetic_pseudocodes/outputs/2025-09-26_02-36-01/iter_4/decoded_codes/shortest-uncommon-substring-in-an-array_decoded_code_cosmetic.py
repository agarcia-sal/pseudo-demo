from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substringsFrequency = defaultdict(int)
        for currentString in arr:
            strLen = len(currentString)
            for startPos in range(strLen):
                for endPos in range(startPos + 1, strLen + 1):
                    fragment = currentString[startPos:endPos]
                    substringsFrequency[fragment] += 1

        results = []
        for sequence in arr:
            seqLen = len(sequence)
            minimalUnique = ""
            for posStart in range(seqLen):
                for posEnd in range(posStart + 1, seqLen + 1):
                    candidate = sequence[posStart:posEnd]
                    if substringsFrequency[candidate] == 1:
                        if (not minimalUnique or
                            len(candidate) < len(minimalUnique) or
                            (len(candidate) == len(minimalUnique) and candidate < minimalUnique)):
                            minimalUnique = candidate
            results.append(minimalUnique)
        return results