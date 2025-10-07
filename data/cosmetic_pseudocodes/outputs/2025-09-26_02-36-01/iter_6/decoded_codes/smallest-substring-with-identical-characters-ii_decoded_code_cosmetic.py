class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            totalOperations = 0
            segmentLength = 0

            def recursiveCheck(index: int) -> bool:
                nonlocal totalOperations, segmentLength
                if index >= len(s):
                    return totalOperations <= numOps

                segmentLength += 1
                atEnd = index == len(s) - 1
                nextDiffers = (index + 1 < len(s) and s[index] != s[index + 1])

                if atEnd or nextDiffers:
                    increments = (segmentLength // m) + 1
                    totalOperations += increments
                    if totalOperations > numOps:
                        return False
                    segmentLength = 0

                return recursiveCheck(index + 1)

            return recursiveCheck(0)

        strLength = len(s)
        lowBound = 1
        highBound = strLength

        def binarySearch(low: int, high: int) -> int:
            if low >= high:
                return low
            middle = low + (high - low) // 2
            if check(middle):
                return binarySearch(low, middle)
            else:
                return binarySearch(middle + 1, high)

        return binarySearch(lowBound, highBound)