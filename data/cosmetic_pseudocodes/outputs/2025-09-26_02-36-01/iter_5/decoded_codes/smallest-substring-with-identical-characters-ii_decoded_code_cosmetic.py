class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            def process(index: int, groupCount: int, totalOps: int) -> int:
                if index >= len(s):
                    return totalOps
                nextIndex = index + 1
                isEndGroup = (nextIndex == len(s)) or (s[index] != s[nextIndex])
                newGroupCount = groupCount + 1
                if isEndGroup:
                    # Calculate operations needed for this group
                    opsAdded = (newGroupCount - 1) // m + 1
                    newTotalOps = totalOps + opsAdded
                    if newTotalOps > numOps:
                        return newTotalOps
                    else:
                        return process(nextIndex, 0, newTotalOps)
                else:
                    return process(nextIndex, newGroupCount, totalOps)

            operationsCount = process(0, 0, 0)
            return operationsCount <= numOps

        lengthStr = len(s)
        low, high = 1, lengthStr

        def binarySearch(lowVal: int, highVal: int) -> int:
            if lowVal == highVal:
                return lowVal
            midpoint = lowVal + (highVal - lowVal) // 2
            if check(midpoint):
                return binarySearch(lowVal, midpoint)
            else:
                return binarySearch(midpoint + 1, highVal)

        result = binarySearch(low, high)
        return result