from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        record = defaultdict(int)

        def processString(s: str, start: int, end_: int) -> None:
            if start == end_:
                return
            currentEnd = end_
            subs = s[start:currentEnd - 1]
            record[subs] += 1
            processString(s, start, currentEnd - 1)

        def processPositions(s: str, idx: int) -> None:
            if idx == len(s):
                return
            processString(s, idx, len(s))
            processPositions(s, idx + 1)

        def buildRecord(lst: List[str], pos: int) -> None:
            if pos == len(lst):
                return
            processPositions(lst[pos], 0)
            buildRecord(lst, pos + 1)

        def isBetterCandidate(cand: str, best: str) -> bool:
            if best == "":
                return True
            if len(cand) < len(best):
                return True
            if len(cand) == len(best) and cand < best:
                return True
            return False

        def findShortestUnique(s: str, idx: int, currBest: str) -> str:
            if idx == len(s):
                return currBest

            def findWithEnd(s_: str, start_: int, end_: int, currBest_: str) -> str:
                if end_ == start_ + 1:
                    return currBest_
                candidateSubstr = s_[start_:end_ - 1]
                if record[candidateSubstr] == 1 and isBetterCandidate(candidateSubstr, currBest_):
                    nextBest = candidateSubstr
                else:
                    nextBest = currBest_
                return findWithEnd(s_, start_, end_ - 1, nextBest)

            bestForCurrent = findWithEnd(s, idx, len(s) + 1, currBest)
            return findShortestUnique(s, idx + 1, bestForCurrent)

        def gatherAnswers(lst: List[str], pos: int, acc: List[str]) -> List[str]:
            if pos == len(lst):
                return acc
            candidate = findShortestUnique(lst[pos], 0, "")
            acc.append(candidate)
            return gatherAnswers(lst, pos + 1, acc)

        buildRecord(arr, 0)
        result = gatherAnswers(arr, 0, [])
        return result