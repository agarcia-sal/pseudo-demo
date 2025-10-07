from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> float:
        resultVar = -1e100
        combos = []
        alphabetStr = "zeroonetwothreefour"

        def buildPairs(idx1: int, idx2: int) -> None:
            if idx1 >= len(alphabetStr):
                return
            if idx2 >= len(alphabetStr):
                buildPairs(idx1 + 1, 0)
                return
            if idx1 != idx2:
                combos.append((alphabetStr[idx1], alphabetStr[idx2]))
            buildPairs(idx1, idx2 + 1)

        buildPairs(0, 0)
        lenS = len(s)

        def processPair(pairA: str, pairB: str) -> None:
            nonlocal resultVar
            mapping = defaultdict(lambda: 1e100)
            prefixCountA = [0]
            prefixCountB = [0]
            boundL = 0

            def handlePosition(idx: int) -> None:
                nonlocal boundL, resultVar
                charC = s[idx]
                nextCountA = prefixCountA[-1] + 1 if charC == pairA else 0
                prefixCountA.append(nextCountA)
                nextCountB = prefixCountB[-1] + 1 if charC == pairB else 0
                prefixCountB.append(nextCountB)

                # Move boundL forward while conditions are satisfied
                while (idx - boundL + 1) >= k and prefixCountA[boundL] < prefixCountA[-1] and prefixCountB[boundL] < prefixCountB[-1]:
                    keyTuple = (prefixCountA[boundL] % 2, prefixCountB[boundL] % 2)
                    prevVal = mapping[keyTuple]
                    candVal = prefixCountA[boundL] - prefixCountB[boundL]
                    if candVal < prevVal:
                        mapping[keyTuple] = candVal
                    boundL += 1

                lastA = prefixCountA[-1]
                lastB = prefixCountB[-1]
                parityKey = ((1 - (lastA % 2)), (lastB % 2))
                candidate = lastA - lastB - mapping[parityKey]
                if candidate > resultVar:
                    resultVar = candidate

            def iterateThrough(iterIdx: int) -> None:
                if iterIdx == lenS:
                    return
                handlePosition(iterIdx)
                iterateThrough(iterIdx + 1)

            iterateThrough(0)

        def idxPairs(pairIdx: int) -> None:
            if pairIdx == len(combos):
                return
            currentPair = combos[pairIdx]
            processPair(currentPair[0], currentPair[1])
            idxPairs(pairIdx + 1)

        idxPairs(0)

        return resultVar