class Solution:
    def minChanges(self, count: list[int]) -> int:
        n = len(count)
        table = [0] * (len(count) + 2)

        def processIndex(curr: int, limit: int) -> None:
            if curr > limit:
                return

            firstVal = count[curr]
            secondVal = count[-curr - 1]

            if firstVal > secondVal:
                firstVal, secondVal = secondVal, firstVal

            table[0] += 1

            diff1 = secondVal - firstVal
            table[diff1] -= 1

            diff2 = diff1 + 1
            table[diff2] += 1

            maxVal = firstVal
            if secondVal > maxVal:
                maxVal = secondVal

            index1 = maxVal + (len(count) - firstVal) + 1
            table[index1] -= 1

            index2 = maxVal + (len(count) - firstVal) + 2
            table[index2] += 1

            processIndex(curr + 1, limit)

        processIndex(0, (n // 2) - 1)

        runningSum = 0
        minResult = None
        for val in table:
            runningSum += val
            if minResult is None or runningSum < minResult:
                minResult = runningSum

        return minResult