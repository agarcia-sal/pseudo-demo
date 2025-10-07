class Solution:
    def minLength(self, s: str, numOps: int) -> int:

        def check(m: int) -> bool:
            def isLastIndex(idx: int) -> bool:
                return idx == len(s) - 1

            def charsDiffer(idx: int) -> bool:
                return s[idx] != s[idx + 1]

            counter = 0
            segmentLen = 0
            pos = 0

            def processSegment():
                nonlocal counter
                additions = (segmentLen // m) + 1
                counter += additions

            while pos < len(s):
                segmentLen += 1

                if isLastIndex(pos) or charsDiffer(pos):
                    processSegment()
                    if counter > numOps:
                        return False
                    segmentLen = 0

                pos += 1

            return counter <= numOps

        lengthS = len(s)
        low = 1
        high = lengthS

        def midPoint(a: int, b: int) -> int:
            return a + ((b - a) // 2)

        while low < high:
            mid = midPoint(low, high)
            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low