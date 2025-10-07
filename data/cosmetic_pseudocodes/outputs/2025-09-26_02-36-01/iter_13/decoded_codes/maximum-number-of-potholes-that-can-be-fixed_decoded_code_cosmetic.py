class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def length(s: str) -> int:
            count = 0
            for _ in s:
                count += 1
            return count

        def charAt(text: str, pos: int) -> str:
            return text[pos]

        def substring(text: str, start: int, length_: int) -> str:
            result = ""
            i = start
            while i < start + length_:
                result += charAt(text, i)
                i += 1
            return result

        def indexOf(text: str, ch: str) -> int:
            i = 0
            while i < length(text):
                if charAt(text, i) == ch:
                    return i
                i += 1
            return -1

        def splitSegments(result: list, inp: str, delimiter: str) -> list:
            def recurSplit(res: list, rem: str, delim: str) -> list:
                if rem == "":
                    return res
                idx = indexOf(rem, delim)
                if idx == -1:
                    res.append(rem)
                    return res
                res.append(substring(rem, 0, idx))
                return recurSplit(res, substring(rem, idx + 1, length(rem) - (idx + 1)), delim)
            return recurSplit(result, inp, delimiter)

        def sortAscending(arr: list) -> list:
            swapped = True
            while swapped:
                swapped = False
                for i in range(length(arr) - 1):
                    if length(arr[i]) > length(arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
            return arr

        fixedCount = 0
        remainingBudget = budget
        segments = splitSegments([], road, '.')
        segments = sortAscending(segments)

        def processSegment(segmentsList: list, idx: int):
            nonlocal fixedCount, remainingBudget
            if idx == length(segmentsList):
                return
            segment = segmentsList[idx]
            segLen = length(segment)
            if segLen == 0:
                processSegment(segmentsList, idx + 1)
                return
            cost = segLen + 1
            if cost <= remainingBudget:
                fixedCount += segLen
                remainingBudget -= cost
                processSegment(segmentsList, idx + 1)
                return

            def tryReduce(N: int):
                nonlocal fixedCount, remainingBudget
                if N == 0 or remainingBudget <= 0:
                    return
                cost = N + 1
                if remainingBudget >= cost:
                    fixedCount += N
                    remainingBudget -= cost
                    return
                tryReduce(N - 1)

            tryReduce(segLen)
            processSegment(segmentsList, idx + 1)

        processSegment(segments, 0)
        return fixedCount