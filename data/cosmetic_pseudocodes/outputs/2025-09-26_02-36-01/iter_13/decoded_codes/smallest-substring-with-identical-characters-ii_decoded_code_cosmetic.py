class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            countAccum = 0
            segmentLen = 0

            def helperLoop(index: int) -> bool:
                nonlocal countAccum, segmentLen
                if index >= len(s):
                    return countAccum <= numOps

                segmentLen += 1
                if index == len(s) - 1 or s[index] != s[index + 1]:
                    countAccum += (segmentLen - 1) // m + 1
                    if countAccum > numOps:
                        return False
                    segmentLen = 0

                return helperLoop(index + 1)

            return helperLoop(0)

        lengthStr = len(s)
        lowBound = 1
        highBound = lengthStr

        def binarySearch(left: int, right: int) -> int:
            if left >= right:
                return left

            middle = (left + right) // 2
            if check(middle):
                return binarySearch(left, middle)
            else:
                return binarySearch(middle + 1, right)

        return binarySearch(lowBound, highBound)