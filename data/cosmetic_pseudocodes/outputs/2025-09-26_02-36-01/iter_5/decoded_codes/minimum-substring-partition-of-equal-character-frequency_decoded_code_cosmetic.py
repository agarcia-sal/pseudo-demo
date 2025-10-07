from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        def dfs(pos: int) -> int:
            def decrementFrequency(keyCount: dict, freqMap: dict, charKey: str):
                if charKey in keyCount and keyCount[charKey] != 0:
                    oldCount = keyCount[charKey]
                    freqMap[oldCount] -= 1
                    if freqMap[oldCount] == 0:
                        del freqMap[oldCount]

            def dfsHelper(index: int, cntMap: dict, freqMap: dict, currentMin: int) -> int:
                if index >= n:
                    return currentMin

                cntMapLocal = dict(cntMap)
                freqMapLocal = dict(freqMap)
                minAns = currentMin

                def recurse(j: int, ansSoFar: int) -> int:
                    if j >= n:
                        return ansSoFar

                    decrementFrequency(cntMapLocal, freqMapLocal, s[j])

                    newCount = cntMapLocal.get(s[j], 0) + 1
                    cntMapLocal[s[j]] = newCount

                    freqMapLocal[newCount] = freqMapLocal.get(newCount, 0) + 1

                    freqKeys = list(freqMapLocal.keys())

                    if len(freqKeys) == 1:
                        tempAns = 1 + dfs(j + 1)
                        if tempAns < ansSoFar:
                            ansSoFar = tempAns

                    return recurse(j + 1, ansSoFar)

                return recurse(index, minAns)

            initialCnt = {}
            initialFreq = {}
            defaultAnswer = n - pos

            answer = dfsHelper(pos, initialCnt, initialFreq, defaultAnswer)

            return answer

        return dfs(0)