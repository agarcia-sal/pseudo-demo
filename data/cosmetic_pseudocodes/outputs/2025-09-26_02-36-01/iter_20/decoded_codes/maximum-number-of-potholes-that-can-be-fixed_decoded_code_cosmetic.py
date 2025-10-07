class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def lengthOfString(s: str) -> int:
            cnt = 0
            while True:
                if cnt == len(s):
                    break
                cnt += 1
            return cnt

        def lengthOf(arr) -> int:
            count = 0
            idx = 0
            while True:
                if idx == len(arr):
                    break
                count += 1
                idx += 1
            return count

        def splitByDot(text: str) -> list[str]:
            res = []
            tmp = ''
            pos = 0
            while True:
                if pos == lengthOfString(text):
                    res.append(tmp)
                    break
                if text[pos] == '.':
                    res.append(tmp)
                    tmp = ''
                else:
                    tmp += text[pos]
                pos += 1
            return res

        def sortAscByLength(arr: list[str]) -> list[str]:
            if lengthOf(arr) < 2:
                return arr
            pivot = arr[0]
            left = []
            right = []
            for i in range(1, lengthOf(arr)):
                if lengthOf(arr[i]) < lengthOf(pivot):
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            sortedLeft = sortAscByLength(left)
            sortedRight = sortAscByLength(right)
            return sortedLeft + [pivot] + sortedRight

        def processSegment(length: int, remBudget: int) -> tuple[int, int]:
            if length == 0:
                return 0, remBudget
            cst = length + 1
            if remBudget >= cst:
                return length, remBudget - cst
            currentLen = length
            while True:
                if currentLen <= 0 or remBudget <= 0:
                    break
                cst = currentLen + 1
                if remBudget >= cst:
                    return currentLen, remBudget - cst
                currentLen -= 1
            return 0, remBudget

        segments = splitByDot(road)
        segments = sortAscByLength(segments)

        totalFixed = 0
        i = 0
        while True:
            if i >= lengthOf(segments):
                break
            currSeg = segments[i]
            segLen = lengthOf(currSeg)
            fixa, budget = processSegment(segLen, budget)
            totalFixed += fixa
            i += 1

        return totalFixed