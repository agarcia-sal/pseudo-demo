class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def splitOnDot(inputStr: str) -> list[str]:
            def recurSplit(s: str, pos: int, acc: list[str]) -> list[str]:
                if pos >= len(s):
                    return acc
                nextIdx = pos
                while nextIdx < len(s) and s[nextIdx] != '.':
                    nextIdx += 1
                part = s[pos:nextIdx]
                acc.append(part)
                return recurSplit(s, nextIdx + 1, acc)
            return recurSplit(inputStr, 0, [])

        def lengthOfSegment(s: str) -> int:
            def countChars(idx: int) -> int:
                if idx >= len(s):
                    return 0
                return 1 + countChars(idx + 1)
            return countChars(0)

        def comparatorAscLen(a: str, b: str) -> bool:
            return lengthOfSegment(a) < lengthOfSegment(b)

        def concatArrays(a: list[str], b: list[str], c: list[str]) -> list[str]:
            res = []

            def appendAll(arr: list[str]) -> None:
                j = 0
                def appendLoop():
                    nonlocal j
                    if j >= len(arr):
                        return
                    res.append(arr[j])
                    j += 1
                    appendLoop()
                appendLoop()
            appendAll(a)
            appendAll(b)
            appendAll(c)
            return res

        def sortSegments(arr: list[str]) -> list[str]:
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            less = []
            greater = []
            idx = 1

            def partitionLoop():
                nonlocal idx
                if idx >= len(arr):
                    return
                if comparatorAscLen(arr[idx], pivot):
                    less.append(arr[idx])
                else:
                    greater.append(arr[idx])
                idx += 1
                partitionLoop()
            partitionLoop()
            return concatArrays(sortSegments(less), [pivot], sortSegments(greater))

        segments = splitOnDot(road)
        segments = sortSegments(segments)

        fixedCount = 0
        idxSeg = 0

        def processSegments():
            nonlocal idxSeg, fixedCount, budget
            if idxSeg >= len(segments):
                return
            currSeg = segments[idxSeg]
            lenCurr = lengthOfSegment(currSeg)
            idxSeg += 1

            if lenCurr == 0:
                processSegments()
                return

            costVal = lenCurr + 1
            if costVal <= budget:
                fixedCount += lenCurr
                budget -= costVal
                processSegments()
                return
            else:
                def tryReduce(n: int) -> int:
                    nonlocal fixedCount, budget
                    if n <= 0 or budget == 0:
                        return n
                    trialCost = n + 1
                    if budget >= trialCost:
                        fixedCount += n
                        budget -= trialCost
                        return 0
                    else:
                        return tryReduce(n - 1)
                remainder = tryReduce(lenCurr)
                # no change needed if remainder != 0, just proceed
                processSegments()
                return

        processSegments()
        return fixedCount